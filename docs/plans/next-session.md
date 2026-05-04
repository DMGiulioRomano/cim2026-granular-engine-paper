# Piano sessione successiva



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


- An **oral communication paper (6–8 pages)**.
- Verifica layout: 2 colonne, Times New Roman 10pt, nessun header/footer
- Anonimizza: rimuovi nome autore e affiliazione per double-blind submission
- Submission via EasyChair entro **7 giugno 2026**
