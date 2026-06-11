# Finestratura come modulazione — perché la copia fedele non è mai esatta

Sintesi da sessione di verifica (2026-06-11) sulla claim di §2.1 del paper
(«lo stream minimo ricostruisce fedelmente il materiale sorgente»): la
formulazione era insostenibile e va sostituita con il rovescio argomentativo —
la finestratura dei grani è una modulazione d'ampiezza, la copia fedele è il
caso limite in cui i prodotti di modulazione quasi si elidono, e il residuo
misurato (−74 dB, fig. 1 del paper) è la firma che lo strumento non è mai
trasparente.

## La tesi DSP

Finestrare un grano significa moltiplicare il segnale per l'inviluppo:
un'operazione di modulazione d'ampiezza, non un prelievo neutro. Le fonti
convergono da tre direzioni indipendenti:

1. **Roads 2001, *Microsound***, sez. *Spectra of Granular Streams* (p. 98):
   con grani a intervalli regolari l'inviluppo complessivo dello stream è
   periodico e il segnale «can be analyzed as a case of *amplitude
   modulation*»; «for each sinusoidal component in the carrier, the periodic
   envelope function contributes a series of *sidebands* to the final
   spectrum», spaziate all'inverso del periodo dell'inviluppo (grani da 20 ms
   → sidebands ogni 50 Hz).
2. **Roads 2001, p. 101** (*Grain Duration Effects*): «The grain envelope
   contributes an amplitude modulation (AM) effect. The modulation spawns
   sidebands around the carrier frequency of the grain at intervals of the
   envelope period. If the grain duration is D, the center frequency of the
   AM is 1/D». Table 3.1: 50 ms (default PGE) → modulazione a 20 Hz,
   «Stable pitch formation».
3. **Keller & Rolfe 1998, *The Corner Effect*** (XII CIM, pp. 236–239,
   [[keller-rolfe1998]]): analisi degli artefatti spettrali della finestra
   (comb dai «corners» del trapezio); riportata anche da Roads 2001 p. 88:
   «the frequency response is similar to that of a Gaussian window, with the
   addition of comb-shaped spectral effects. Null points in the spectrum are
   proportional to the position of the corners of the window». Tesi del
   paper: «what has been regarded as an unwanted artifact by DSP theory,
   becomes a useful parameter for sound synthesis» (p. 239).
4. **Dutilleux et al. 2016, p. 110** ([[dutilleux2016]]): grani a istanti
   regolari con forma d'onda correlata = «treno di impulsi filtrati», suono
   periodico il cui inviluppo spettrale è determinato dalla forma del grano.
5. **De Poli & Piccialli 1988, p. 70** ([[depoli-piccialli1988]]):
   «inviluppo ≡ finestra di analisi» — la stessa identità letta dal lato
   analisi.

## Perché il residuo del paper è −74 dB (verifica numerica 2026-06-11)

La condizione di somma costante (COLA) per la Hann a overlap 2 vale in forma
esatta solo per la finestra **periodica** (denominatore N). PGE genera le
finestre con `np.hanning(n)` (`rendering/numpy_window_registry.py`), la
variante **simmetrica** (denominatore N−1); gli onset sono quantizzati al
campione (`round(onset·sr)`, `rendering/numpy_audio_renderer.py`).

Misura OLA (regione a regime, 40 grani):

| Finestra | N | hop | ripple RMS | dB |
|---|---|---|---|---|
| `np.hanning` simmetrica | 2400 (48 kHz, 50 ms) | 1200 | 2.02·10⁻⁴ | **−73.9** |
| Hann periodica | 2400 | 1200 | 1.5·10⁻¹⁶ | −316 (precisione macchina) |
| `np.hanning` simmetrica | 2205 (44.1 kHz, 50 ms) | 1102 | 2.2·10⁻¹⁶ | esatta (N dispari: hop = (N−1)/2) |

Il ripple −73.9 dB della simmetrica a N pari coincide col residuo RMS
gain-matched −74 dB della fig. 1 del paper: il residuo è interamente
spiegato dalla COLA approssimata. Curiosità: a N dispari la simmetrica è
esatta perché hop = (N−1)/2 centra il periodo N−1.

Il ripple è un'AM residua a 1/IOT (40 Hz a hop 25 ms): bande laterali a
≈−74 dB attorno a ogni componente. È il caso di elisione quasi completa; il
comb di [[time-stretching-granulare]] (`offset = (1−s)·IOT`) è cosa succede
quando la cancellazione si rompe del tutto.

## Onestà matematica (vincolo di formulazione)

Con Hann periodica, hop intero in campioni e lettura allineata la
ricostruzione OLA sarebbe esatta in aritmetica esatta. Quindi **non**
scrivere «impossibile in assoluto»: la formulazione corretta è che la
finestratura è sempre una modulazione i cui prodotti si elidono solo nel
caso ideale; la copia fedele è il caso degenere di questa elisione, fragile
per costruzione (qualunque scostamento — speed≠1, jitter, trasposizione —
la rompe) e mai esatta nell'implementazione reale.

## Implicazione argomentativa per il paper

§2.1 riformulata (2026-06-11): «i default sono scelti perché lo stream
minimo *approssimi al meglio* il materiale sorgente»; la finestratura è
modulazione (cit. `Roads2001`, `KellerRolfe1998`); il residuo −74 dB è la
misura dell'elisione imperfetta; «la copia fedele non è la sospensione della
granulazione ma il suo caso limite: anche il grado zero finestra, somma e
modula». La footnote collega il residuo al ripple di somma della finestra
implementata e rinvia a §\ref{sec:pointer} per la rottura della
cancellazione (ronzio del freeze di ex2).

Rafforza la tesi centrale: il sistema non è mai trasparente nemmeno al grado
zero — coerente con la postura per cui ogni specifica è già un atto di
granulazione, e con la linea Keller-Rolfe → [[decorrelazione-granulare]]
(l'artefatto che la teoria DSP scarta diventa parametro compositivo).

## Sezioni del paper CIM 2026 dove usare

- **§ stream minimo (sec:stream-minimo)**: già integrato (riformulazione
  2026-06-11 con cit. Roads2001 + KellerRolfe1998).
- **Sezione 2**: eventuale richiamo all'AM dell'inviluppo (Roads p. 101,
  Table 3.1) parlando di durata di grano e formazione del pitch.
- **Da non fare**: promettere ricostruzione bit-identica della sorgente in
  qualunque punto del paper (cfr. memoria di progetto su riproducibilità
  per andamento).

## Pagine collegate

[[time-stretching-granulare]] · [[decorrelazione-granulare]] ·
[[keller-rolfe1998]] · [[dutilleux2016]] · [[depoli-piccialli1988]] ·
[[roads2001-ch03-granular-synthesis]]
