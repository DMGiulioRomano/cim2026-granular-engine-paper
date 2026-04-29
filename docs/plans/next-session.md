# Piano sessione successiva

## 0. Contesto tecnico disponibile

PythonGranularEngine è già clonato in `../PythonGranularEngine` (relativo alla root di questo repo).
Punto di partenza per studiarlo:
- `../PythonGranularEngine/CLAUDE.md` — panoramica architettura
- `../PythonGranularEngine/docs/*.md` — documentazione tecnica dettagliata
- Tutto il sorgente Python è leggibile direttamente per dettagli precisi (nomi classi, parametri, formule)

---

## 1. Analizza atti CIM 2024

**Priorità: alta — da fare prima di scrivere.**

Leggi 2–3 paper demo da `proceedings/CIM2024_XXIV_Atti.pdf`.  
Obiettivo: calibrare tono, densità tecnica, struttura tipica dei demo a 4 pagine.  
Aggiorna `CLAUDE.md` con i risultati (livello accademico osservato, struttura prevalente).

---

## 2. Studia PythonGranularEngine

Leggi `../PythonGranularEngine/CLAUDE.md` e `../PythonGranularEngine/docs/*.md`.  
Poi approfondisci il sorgente per estrarre:
- Nomi esatti di classi e metodi (Grain, Stream, Cartridge, renderer)
- Parametri YAML con esempi reali
- Formula overlap-add usata dal renderer NumPy
- Logica SHA-256 cache

Necessario per scrivere la sezione architettura senza approssimazioni.

---

## 3. Scrivi abstract

150–200 parole, in inglese (obbligatorio anche se paper in italiano).  
Prima cosa da fissare — vincola struttura e contributi di tutto il paper.

---

## 4. Scrivi sezioni in ordine

1. Introduzione — contesto, tool esistenti (CSound, SuperCollider, Max/MSP, pyo), motivazione Python deferred
2. Fondamenti della sintesi granulare — grano, densità, involucro, pitch ratio, scatter
3. Architettura del sistema — Grain/Stream/Cartridge, YAML DSL, dual renderer, cache
4. Notazione grafica generata — Y=buffer position, colore=pitch, opacità=volume
5. Dimostrazione — esperimento densità 4–300 grains/sec, 9 sezioni, soglie percettive
6. Conclusioni e sviluppi futuri

---

## 5. Produci figure

- Schema architettura: YAML → engine → (NumPy renderer | Csound renderer) → audio + graphic score
- Screenshot graphic score reale (da output del repo)
- Plot o tabella dell'esperimento densità (sezioni, densità, parametri variati)

Figure devono essere leggibili in B&W (stampa proceedings).

---

## 6. Referenze

Già presenti in `paper.tex`: Roads 1978/2001, Truax 1988, Xenakis 1971.  
Da aggiungere:
- Strumenti Python audio comparabili: pyo, librosa, pedalboard, scipy.signal
- Paper su sintesi granulare interattiva/real-time (per differenziare il contributo)
- 1–2 paper da atti CIM recenti su tool simili (coerenza col venue)

Target: 12–18 referenze totali.

---

## 7. Zenodo DOI (opzionale ma consigliato)

Deposita PythonGranularEngine su [Zenodo](https://zenodo.org) per ottenere DOI citabile nel paper.  
Aumenta credibilità e riproducibilità — standard nei paper CIM recenti.

---

## 8. Check finale

- Conta pagine compiled PDF (max 4 — demo category)
- Verifica layout: 2 colonne, Times New Roman 10pt, nessun header/footer
- Anonimizza: rimuovi nome autore e affiliazione per double-blind submission
- Submission via EasyChair entro **7 giugno 2026**
