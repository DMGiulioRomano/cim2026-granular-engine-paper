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
DEVIATION_DIR := $(EX_DIR)/deviation
DEVIATION_AIF := $(DEVIATION_DIR)/deviation__mask_range.aif
DEVIATION_MAP := $(DEVIATION_DIR)/deviation_map.pdf

.PHONY: all venv install graph clean-graph clean examples examples-clean paper clean-latex link-refs cite-map jitter-table

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

graph: install
	mkdir -p $(GRAPH_DIR)
	$(VENV)/bin/pyan3 $(shell find $(PGE_SRC) -name "*.py") \
		--dot --no-defines 2>/dev/null > $(GRAPH_DIR)/call_graph.dot
	cd $(PGE_DIR) && \
		$(VENV)/bin/py2puml src src \
		> $(GRAPH_DIR)/class_diagram.puml 2>/dev/null || true

# examples è prerequisito: i PDF figura non sono tracciati in git (stocastici),
# vanno rigenerati prima di compilare il paper che li \include.
paper: clean-latex link-refs examples jitter-table $(PAPER_DIR)/paper.tex $(PAPER_DIR)/refs.bib
	cd $(PAPER_DIR) && latexmk -pdf -bibtex -interaction=nonstopmode -halt-on-error paper.tex

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

# examples: per ogni exN.yml renderizza audio + partitura (PGE pinnato) e
# genera waveform + spettrogramma B&W-safe dall'.aif. Richiede weNeedToTalkAboutIt.wav in
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

# examples: rigenera SOLO gli esempi il cui .yml (o gli script) è cambiato.
# Make confronta i timestamp: un .aif più recente del suo .yml non viene
# rirenderizzato. Per forzare tutto: `make examples-clean examples`.
# Rendering stocastico: stesso ANDAMENTO a ogni run, non bit-identico.
examples: $(EX_AIFS) $(EX_PLOTS) $(COMPARISON) $(DEVIATION_AIF) $(DEVIATION_MAP)
	@echo "=== examples aggiornati ==="

# render: <name>.yml -> <name>.aif + <name>_score.pdf (un'unica invocazione).
# link-refs è order-only (|): serve prima del render ma non forza il rebuild.
$(EX_DIR)/%.aif: $(EX_DIR)/%.yml $(EX_DIR)/render_example.py | install link-refs
	@echo "=== render $< ==="
	$(PYTHON) $(EX_DIR)/render_example.py $<

# plot: <name>.aif -> <name>_waveform.pdf + <name>_spectrogram.pdf (un'unica
# invocazione: il target spettrogramma fa da proxy anche per il waveform).
$(EX_DIR)/%_spectrogram.pdf: $(EX_DIR)/%.aif $(EX_DIR)/plot.py
	@echo "=== plot $< ==="
	$(PYTHON) $(EX_DIR)/plot.py $<

# deviation: STEMS-only, due gemelli (mask_range + mask_dephase) renderizzati
# in un'unica invocazione. deviation__mask_range.aif tracciato da make come
# rappresentante; deviation__mask_dephase.aif e deviation_map.pdf (non annotata)
# sono side-effect della stessa invocazione.
$(DEVIATION_AIF): $(DEVIATION_DIR)/deviation.yml $(EX_DIR)/render_example.py | install link-refs
	@echo "=== render (STEMS) $< ==="
	STEMS=1 $(PYTHON) $(EX_DIR)/render_example.py $<

# annota deviation_map.pdf con le lettere di pannello (a)/(b); ri-genera ogni
# volta che cambia deviation.yml o il render STEMS di cui dipende.
$(DEVIATION_MAP): $(DEVIATION_DIR)/deviation.yml $(EX_DIR)/annotate_panels.py | $(DEVIATION_AIF)
	@echo "=== annotate panels deviation ==="
	$(PYTHON) $(EX_DIR)/annotate_panels.py $<

# comparison: dipende dall'.aif di identity + dal wav originale + dallo script.
$(COMPARISON): $(EX_DIR)/identity/identity.aif $(EX_DIR)/plot_comparison.py
	@echo "=== comparison plot identity ==="
	$(PYTHON) $(EX_DIR)/plot_comparison.py \
		$(EX_DIR)/identity/identity.aif \
		$(PGE_REFS)/weNeedToTalkAboutIt.wav \
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
