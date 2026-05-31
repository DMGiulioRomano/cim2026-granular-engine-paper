REPO_DIR  := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
VENV      := $(REPO_DIR).venv
PYTHON    := $(VENV)/bin/python
PIP       := $(VENV)/bin/pip
PGE_DIR   := $(REPO_DIR)raw/PythonGranularEngine
PGE_SRC   := $(PGE_DIR)/src
GRAPH_DIR   := $(REPO_DIR)graph
CONTEXT_DIR := $(REPO_DIR)context
PAPERS_DIR  := $(REPO_DIR)raw/papers
PROC_DIR    := $(REPO_DIR)raw/proceedings
PAPER_DIR   := $(REPO_DIR)paper
EX_DIR      := $(PAPER_DIR)/examples
EX_YMLS     := $(wildcard $(EX_DIR)/*/ex*.yml)

.PHONY: all venv install graph clean-graph clean examples examples-clean paper clean-latex

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

paper: $(PAPER_DIR)/paper.tex $(PAPER_DIR)/refs.bib
	cd $(PAPER_DIR) && pdflatex paper.tex
	cd $(PAPER_DIR) && bibtex paper
	cd $(PAPER_DIR) && pdflatex paper.tex
	cd $(PAPER_DIR) && pdflatex paper.tex

# examples: per ogni exN.yml renderizza audio + partitura (PGE pinnato) e
# genera waveform + spettrogramma B&W-safe dall'.aif. Richiede pino2.wav in
# raw/PythonGranularEngine/refs/ (gitignored). Rendering stocastico: stesso
# ANDAMENTO a ogni run, non bit-identico (vedi paper/examples/README.md).
examples: install
	@for yml in $(EX_YMLS); do \
		echo "=== render $$yml ==="; \
		$(PYTHON) $(EX_DIR)/render_example.py $$yml || exit 1; \
		stem=$${yml%.yml}; \
		$(PYTHON) $(EX_DIR)/plot.py $${stem}.aif || exit 1; \
	done

examples-clean:
	rm -f $(EX_DIR)/*/*.aif $(EX_DIR)/*/*_score.pdf \
	      $(EX_DIR)/*/*_waveform.pdf $(EX_DIR)/*/*_spectrogram.pdf

clean-graph:
	rm -f $(GRAPH_DIR)/call_graph.dot $(GRAPH_DIR)/class_diagram.puml

clean: clean-graph
	rm -rf $(VENV)

clean-latex:
	rm -f $(PAPER_DIR)/paper.aux $(PAPER_DIR)/paper.log $(PAPER_DIR)/paper.out \
	$(PAPER_DIR)/paper.toc $(PAPER_DIR)/paper.bbl $(PAPER_DIR)/paper.blg \
	$(PAPER_DIR)/paper.fls $(PAPER_DIR)/paper.fdb_latexmk \
	$(PAPER_DIR)/paper.synctex.gz $(PAPER_DIR)/paper.pdf
