# CIM 2026 — Demo Paper: PythonGranularEngine

**XXV Colloquio di Informatica Musicale** — L'Aquila, 13–16 Ottobre 2026  
**Tema:** Sounding the Posthuman  
**Categoria:** Demo (max 4 pagine)

## Scadenze

| Evento | Data |
|--------|------|
| EasyChair apre | 28 febbraio 2026 |
| **Submission deadline** | **7 giugno 2026** |
| Notifica accettazione | 15 luglio 2026 |
| Camera-ready | 31 agosto 2026 |

## Struttura repository

```
paper.tex          — sorgente LaTeX principale
templates/         — template ufficiale CIM 2026 (PDF + ODT)
proceedings/       — atti CIM 2022 e 2024 (esclusi da git, troppo grandi)
resources/         — figure, audio examples, screenshot
```

## Compilazione

```bash
pdflatex paper.tex
pdflatex paper.tex   # seconda pass per riferimenti incrociati
```

## Template ufficiale

- PDF: `templates/cim2026_template_paper.pdf`
- ODT: `templates/cim2026_template_paper.odt`
- Fonte: https://musel.consaq.it/cim2026/contributions/papers/

## Submission

Via EasyChair: https://easychair.org/conferences/?conf=xxvcim2026  
Lingua: italiano o inglese (abstract in inglese obbligatorio)  
Formato: PDF anonimizzato (double-blind review)

## Progetto descritto

[PythonGranularEngine](https://github.com/DMGiulioRomano/PythonGranularEngine) —
granulatore in tempo differito scritto interamente in Python.
