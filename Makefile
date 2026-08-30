REPO_DIR  := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
VENV      := $(REPO_DIR).venv
PYTHON    := $(VENV)/bin/python
PIP       := $(VENV)/bin/pip
PGE_DIR   := $(REPO_DIR)raw/PythonGranularEngine
PGE_SRC   := $(PGE_DIR)/src
# refs/ del repo PGE reale: sibling del repo padre, override con env PGE_REFS
PGE_REFS  ?= $(abspath $(REPO_DIR)../PythonGranularEngine/refs)
PGE_DEST  := $(PGE_DIR)/refs
GRAPH_DIR   := $(REPO_DIR)graph
CONTEXT_DIR := $(REPO_DIR)context
PAPERS_DIR  := $(REPO_DIR)raw/papers
PROC_DIR    := $(REPO_DIR)raw/proceedings
PAPER_DIR   := $(REPO_DIR)paper
EX_DIR      := $(PAPER_DIR)/examples
FIG_DIR     := $(PAPER_DIR)/figures
# Un esempio per cartella: <token>/<token>.yml (token semantico, niente numeri;
# l'ordine di lettura vive solo in paper.tex). deviation/ e' STEMS-only (due
# gemelli, due audio separati, niente <token>.aif singolo): gestita da regole
# dedicate sotto, esclusa dal pattern generico %.aif/%_spectrogram.pdf.
EX_YMLS     := $(filter-out $(EX_DIR)/deviation/%,$(wildcard $(EX_DIR)/*/*.yml))
EX_AIFS     := $(EX_YMLS:.yml=.aif)
EX_PLOTS    := $(EX_YMLS:.yml=_spectrogram.pdf)
COMPARISON  := $(EX_DIR)/identity/identity_comparison.pdf
JITTER_TEX  := $(FIG_DIR)/jitter_table.tex
GRAMMAR_TEX := $(FIG_DIR)/grammar_tree.tex
DEVIATION_DIR := $(EX_DIR)/deviation
DEVIATION_AIF := $(DEVIATION_DIR)/deviation__mask_range.aif
DEVIATION_MAP := $(DEVIATION_DIR)/deviation_annotated.pdf

# Base del diff camera-ready: il tag della versione spedita a EasyChair
# (c30a0d6, 23 giu). NON il merge-base con main — main ha ricevuto la rinomina
# deviation_probability e il bump a PGE v7 il 13 agosto, prima che il branch
# nascesse, e col merge-base la risposta a R1.M5/D24 resterebbe invisibile.
# Per rileggere il solo lavoro recente:
#   make paper-diff DIFF_BASE=$(git merge-base main HEAD)
# Fallback al merge-base se il tag manca (clone senza tag: i tag non seguono
# il fetch di default).
DIFF_BASE ?= $(shell git -C $(REPO_DIR) rev-parse -q --verify cim2026-submitted \
	         || git -C $(REPO_DIR) merge-base main HEAD)
DIFF_OLD  := $(REPO_DIR).diff-base

.PHONY: all venv install graph clean-graph clean examples examples-clean paper paper-diff clean-latex link-refs cite-map jitter-table grammar-tree changelog

# .aif e gli _score.pdf sono prodotti dal render ma usati come input dei plot:
# senza questo make li tratterebbe come "intermediate" e li cancellerebbe a
# fine build (o non li ricostruirebbe se manca solo l'.aif). PRECIOUS li tiene.
.PRECIOUS: $(EX_AIFS) $(DEVIATION_AIF)

all: paper

$(VENV)/bin/activate:
	python3 -m venv $(VENV)

venv: $(VENV)/bin/activate

install: venv
	$(PIP) install --upgrade pip -q
	$(PIP) install -r $(REPO_DIR)requirements.txt -q

# I due tool scrivono su stdout, quindi `> file` TRONCA il file buono prima
# ancora che il tool giri: un fallimento non lascia il diagramma vecchio,
# lascia zero byte. Si scrive su .tmp e si sposta solo a successo.
# Niente `|| true`: nascondeva il fallimento di py2puml su v7 (non digerisce
# le forward reference fra apici, vedi l'intestazione di class_diagram.puml
# e la issue #37) e faceva committare un file vuoto sotto un messaggio che
# dichiarava i grafi rigenerati. Lo stderr di py2puml resta visibile: se
# fallisce, serve sapere perche'.
graph: install
	mkdir -p $(GRAPH_DIR)
	$(VENV)/bin/pyan3 $(shell find $(PGE_SRC) -name "*.py") \
		--dot --no-defines 2>/dev/null > $(GRAPH_DIR)/call_graph.dot.tmp \
		&& mv $(GRAPH_DIR)/call_graph.dot.tmp $(GRAPH_DIR)/call_graph.dot
	cd $(PGE_DIR) && \
		$(VENV)/bin/py2puml src src > $(GRAPH_DIR)/class_diagram.puml.tmp \
		&& mv $(GRAPH_DIR)/class_diagram.puml.tmp $(GRAPH_DIR)/class_diagram.puml

# examples è prerequisito: i PDF figura non sono tracciati in git (stocastici),
# vanno rigenerati prima di compilare il paper che li \include.
paper: clean-latex link-refs examples jitter-table grammar-tree $(PAPER_DIR)/paper.tex $(PAPER_DIR)/refs.bib
	cd $(PAPER_DIR) && latexmk -pdf -bibtex -interaction=nonstopmode -halt-on-error paper.tex

# paper-diff: paper-diff.pdf con le modifiche del branch camera-ready marcate —
# aggiunte in rosso, tagli barrati — via latexdiff contro DIFF_BASE. Strumento
# di rilettura, non di consegna: al comitato va il camera-ready pulito.
# --flatten espande gli \input: latexdiff confronta i due documenti interi.
# Il sed gira in verde scuro il blu di default di \DIFadd (le aggiunte); \DIFdel
# e' gia' rosso barrato. Verde a 0.55 e non puro: sul bianco il verde pieno e'
# illeggibile.
# Non rigenera gli esempi (niente prerequisito examples): le figure risolvono
# dalla paper/ corrente, il vecchio albero serve solo per i sorgenti .tex.
# Il .bbl si rigenera in ENTRAMBI gli alberi prima del confronto. E' gitignored,
# quindi l'albero vecchio non ce l'ha, e --flatten espandeva \bibliography solo
# nel documento nuovo: l'intera bibliografia risultava aggiunta. refs.bib pero'
# e' tracciato, quindi il .bbl vecchio si ricostruisce — -draftmode salta le
# figure (che nell'albero vecchio mancano e avevano altri nomi) e serve solo a
# produrre l'.aux con le \citation da dare in pasto a bibtex.
paper-diff: $(PAPER_DIR)/paper.tex
	rm -rf $(DIFF_OLD)
	mkdir -p $(DIFF_OLD)
	git -C $(REPO_DIR) archive $(DIFF_BASE) paper | tar -x -C $(DIFF_OLD)
	cd $(DIFF_OLD)/paper && pdflatex -interaction=batchmode -draftmode paper.tex >/dev/null 2>&1; bibtex paper >/dev/null 2>&1 || true
	cd $(PAPER_DIR) && pdflatex -interaction=batchmode -draftmode paper.tex >/dev/null 2>&1; bibtex paper >/dev/null 2>&1 || true
	latexdiff --flatten \
		--config "PICTUREENV=(?:picture|DIFnomarkup|lstlisting)[\w\d*@]*" \
		$(DIFF_OLD)/paper/paper.tex $(PAPER_DIR)/paper.tex \
		| sed '/DIFadd/s/\\color{blue}/\\color[rgb]{0,0.55,0}/g' \
		> $(PAPER_DIR)/paper-diff.tex
	cd $(PAPER_DIR) && latexmk -pdf -bibtex -interaction=nonstopmode paper-diff.tex

# changelog: il documento unico da caricare su EasyChair accanto al camera-ready.
# Il comitato chiede "un breve file" (singolare), quindi la lettera di risposta
# alle revisioni e il diff marcato viaggiano in un solo PDF: changelog.tex
# incorpora paper-diff.pdf in appendice via pdfpages, e per questo lo ha come
# prerequisito (e' gitignored, su clone pulito non esiste).
# Il passo ghostscript non e' cosmetico: le map di matplotlib sono vettoriali e
# fitte di poligoni, il PDF esce sui 18 MB e rischia il limite di upload.
# /prepress comprime gli stream senza ricampionare, si scende sotto i 10 MB.
changelog: paper-diff
	cd $(PAPER_DIR) && pdflatex -interaction=nonstopmode changelog.tex >/dev/null
	cd $(PAPER_DIR) && pdflatex -interaction=nonstopmode changelog.tex >/dev/null
	cd $(PAPER_DIR) && gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 \
		-dPDFSETTINGS=/prepress -dNOPAUSE -dQUIET -dBATCH \
		-sOutputFile=changelog-compressed.pdf changelog.pdf \
		&& mv changelog-compressed.pdf changelog.pdf
	@echo "changelog.pdf pronto: $$(du -h $(PAPER_DIR)/changelog.pdf | cut -f1)"

# cite-map: rigenera il blocco meccanico di wiki/concepts/mappa-citazioni-paper.md
# dai \cite{} di paper.tex (marker BEGIN/END, parte editoriale intatta).
# Da rilanciare dopo ogni modifica ai \cite{} del paper.
cite-map:
	python3 $(REPO_DIR)tools/cite_map.py

# jitter-table: rigenera figures/jitter_table.tex (corpo di Tab.~\ref{tab:jitter}
# in sections/24-deviazione.tex) dai default_jitter del PGE pinnato, così i
# numeri stampati non divergono dal codice. Phony: rigenera sempre (import veloce),
# garantendo sincronia anche dopo un bump del submodule. Output gitignored,
# prerequisito di paper. Legge il submodule (raw/PythonGranularEngine/src);
# override con env PGE_SRC. Solo stdlib + import PGE puro: usa python3 di sistema.
jitter-table:
	python3 $(FIG_DIR)/gen_jitter_table.py

# grammar-tree: rigenera figures/grammar_tree.tex, l'albero della grammatica YAML
# (risposta a R1.M6) coi domini derivati dal PGE pinnato. Come jitter-table e'
# phony: rigenera sempre, cosi' un bump del submodule si propaga da solo.
# Se il bump introduce una chiave YAML che lo scheletro dello script non piazza,
# esce con codice 1 e la elenca: il paper non compila con una grammatica
# incompleta invece di stamparla monca in silenzio.
grammar-tree:
	python3 $(FIG_DIR)/gen_grammar_tree.py

# examples: per ogni exN.yml renderizza audio + partitura (PGE pinnato) e
# genera waveform + spettrogramma B&W-safe dall'.aif. Richiede voice.wav in
# raw/PythonGranularEngine/refs/ (gitignored). Rendering stocastico: stesso
# ANDAMENTO a ogni run, non bit-identico (vedi paper/examples/README.md).
# link-refs: ricrea i symlink dei file audio dal repo PGE reale (sibling, refs/)
# dentro la refs/ vuota del submodule. Path dinamico, override con env PGE_REFS.
# Da rilanciare dopo ogni git pull / submodule update (vedi CLAUDE.md).
link-refs:
	@src="$(PGE_REFS)"; dest="$(PGE_DEST)"; \
	if [ ! -d "$$src" ]; then \
		echo "errore: refs sorgente non trovata: $$src" >&2; \
		echo "        setta PGE_REFS, es: PGE_REFS=/path/to/PythonGranularEngine/refs make link-refs" >&2; \
		exit 1; \
	fi; \
	mkdir -p "$$dest"; \
	for link in "$$dest"/*; do \
		if [ -L "$$link" ] && [ ! -e "$$link" ]; then rm -f "$$link"; fi; \
	done; \
	count=0; \
	for f in "$$src"/*; do \
		[ -f "$$f" ] || continue; \
		name="$$(basename "$$f")"; \
		case "$$name" in .gitkeep|.DS_Store) continue ;; esac; \
		ln -sf "$$f" "$$dest/$$name"; \
		count=$$((count + 1)); \
	done; \
	echo "link-refs: $$count symlink in $$dest -> $$src"

# examples: rigenera SOLO gli esempi il cui .yml (o gli script, o il commit
# pinnato del submodule PGE) è cambiato. Make confronta i timestamp: un .aif
# più recente di tutti i suoi prerequisiti non viene rirenderizzato.
# Per forzare tutto comunque: `make examples-clean examples`.
# Rendering stocastico: stesso ANDAMENTO a ogni run, non bit-identico.
examples: $(EX_AIFS) $(EX_PLOTS) $(COMPARISON) $(DEVIATION_AIF) $(DEVIATION_MAP)
	@echo "=== examples aggiornati ==="

# PGE_STAMP: il commit pinnato del submodule, come lo vede git (`git submodule
# status`), scritto su file SOLO se e' cambiato dall'ultima volta. La recipe
# gira sempre (prerequisito .PHONY-like FORCE) ma tocca il file solo a hash
# diverso, cosi' i target a valle (che dipendono da PGE_STAMP) non si
# rirenderizzano ad ogni `make examples` — solo quando il submodule avanza.
PGE_STAMP := $(REPO_DIR).pge-commit-stamp
.PHONY: FORCE
FORCE:
$(PGE_STAMP): FORCE
	@git -C $(REPO_DIR) submodule status raw/PythonGranularEngine \
		| awk '{print $$1}' > $@.tmp
	@cmp -s $@.tmp $@ 2>/dev/null && rm -f $@.tmp || mv $@.tmp $@

# render: <name>.yml -> <name>.aif + <name>_score.pdf (un'unica invocazione).
# link-refs è order-only (|): serve prima del render ma non forza il rebuild.
$(EX_DIR)/%.aif: $(EX_DIR)/%.yml $(EX_DIR)/render_example.py $(PGE_STAMP) | install link-refs
	@echo "=== render $< ==="
	$(PYTHON) $(EX_DIR)/render_example.py $<

# plot: <name>.aif -> <name>_waveform.pdf + <name>_spectrogram.pdf (un'unica
# invocazione: il target spettrogramma fa da proxy anche per il waveform).
# distribution: spettrogramma e MAP sono impilati in Fig. 2 (sec:griglia),
# --align-map allinea l'asse x del pannello tempo ai bordi della MAP.
$(EX_DIR)/distribution/distribution_spectrogram.pdf: $(EX_DIR)/distribution/distribution.aif $(EX_DIR)/plot.py
	@echo "=== plot $< (align-map) ==="
	$(PYTHON) $(EX_DIR)/plot.py $< --align-map

$(EX_DIR)/%_spectrogram.pdf: $(EX_DIR)/%.aif $(EX_DIR)/plot.py
	@echo "=== plot $< ==="
	$(PYTHON) $(EX_DIR)/plot.py $<

# deviation: STEMS-only, due gemelli (mask_range + mask_probability) renderizzati
# in un'unica invocazione. deviation__mask_range.aif tracciato da make come
# rappresentante; deviation__mask_probability.aif e deviation_map.pdf (non annotata)
# sono side-effect della stessa invocazione.
$(DEVIATION_AIF): $(DEVIATION_DIR)/deviation.yml $(EX_DIR)/render_example.py $(PGE_STAMP) | install link-refs
	@echo "=== render (STEMS) $< ==="
	STEMS=1 $(PYTHON) $(EX_DIR)/render_example.py $<

# annota deviation_map.pdf con le lettere di pannello (a)/(b); ri-genera ogni
# volta che cambia deviation.yml o il render STEMS di cui dipende.
DEVIATION_MAP := $(DEVIATION_DIR)/deviation_annotated.pdf

$(DEVIATION_MAP): $(DEVIATION_DIR)/deviation.yml $(EX_DIR)/annotate_panels.py $(DEVIATION_AIF)
	@echo "=== annotate panels deviation ==="
	$(PYTHON) $(EX_DIR)/annotate_panels.py $< --output $@
	
# comparison: dipende dall'.aif di identity + dal wav originale + dallo script.
$(COMPARISON): $(EX_DIR)/identity/identity.aif $(EX_DIR)/plot_comparison.py
	@echo "=== comparison plot identity ==="
	$(PYTHON) $(EX_DIR)/plot_comparison.py \
		$(EX_DIR)/identity/identity.aif \
		$(PGE_REFS)/voice.wav \
		--duration 2.0

examples-clean:
	rm -f $(EX_DIR)/*/*.aif $(EX_DIR)/*/*_score.pdf \
	      $(EX_DIR)/*/*_waveform.pdf $(EX_DIR)/*/*_spectrogram.pdf \
	      $(EX_DIR)/*/*_comparison.pdf $(JITTER_TEX)

clean-graph:
	rm -f $(GRAPH_DIR)/call_graph.dot $(GRAPH_DIR)/class_diagram.puml

clean: clean-graph
	rm -rf $(VENV)

clean-latex:
	rm -f $(PAPER_DIR)/paper.aux $(PAPER_DIR)/paper.log $(PAPER_DIR)/paper.out \
	$(PAPER_DIR)/paper.toc $(PAPER_DIR)/paper.bbl $(PAPER_DIR)/paper.blg \
	$(PAPER_DIR)/paper.fls $(PAPER_DIR)/paper.fdb_latexmk \
	$(PAPER_DIR)/paper.synctex.gz $(PAPER_DIR)/paper.pdf
