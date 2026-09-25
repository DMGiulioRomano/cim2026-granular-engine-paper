# Finestratura come modulazione — perché la copia fedele non è mai esatta

> **Posizione del paper consegnato** (`sec:c-e`): «Lo stato corrente coincide
> con la trasformazione identica della sorgente: questa configurazione
> garantisce una risintesi a guadagno unitario e inalterata», con la nota
> «Finestrare un grano ne modula l'ampiezza, aggiungendo allo spettro bande
> laterali~\cite{Roads2001}. Nella sovrapposizione a fattore 2 questi contributi
> si elidono.» Il paper non mostra il residuo: `fig:c-e` è la MAP di `identity`,
> non il confronto (`identity_comparison.pdf` esiste ma non è incluso).
>
> **Discrepanza aperta.** La misura sotto (−73,9 dB con `np.hanning`
> simmetrica, N = 2400 a 48 kHz, la frequenza di uscita degli esempi) dice che
> l'elisione è quasi completa, non esatta. «Inalterata» e «si elidono» nel
> paper sono quindi un'approssimazione.

Sintesi da sessione di verifica (2026-06-11) su una versione precedente del
paper, che sosteneva la ricostruzione fedele. La formulazione proposta allora
(la finestratura è una modulazione d'ampiezza, la copia fedele è il caso
limite in cui i prodotti di modulazione quasi si elidono, il residuo misurato
è la firma che lo strumento non è mai trasparente) **non è entrata nel paper
consegnato**.

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

## Perché il residuo è −74 dB (verifica numerica 2026-06-11)

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
gain-matched −74 dB misurato su `identity` (la fig. 1 di una versione
precedente del paper, oggi `identity_comparison.pdf`, non inclusa): il residuo
è interamente spiegato dalla COLA approssimata. Curiosità: a N dispari la simmetrica è
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

## Proposta del 2026-06-11 (non adottata nel paper consegnato)

Riformulazione proposta allora per la sezione sullo stream minimo: «i default sono scelti perché lo stream
minimo *approssimi al meglio* il materiale sorgente»; la finestratura è
modulazione (cit. `Roads2001`, `KellerRolfe1998`); il residuo −74 dB è la
misura dell'elisione imperfetta; «la copia fedele non è la sospensione della
granulazione ma il suo caso limite: anche il grado zero finestra, somma e
modula». La footnote proposta collegava il residuo al ripple di somma della finestra
implementata e rinviava a `sec:pointer` per la rottura della cancellazione
(ronzio del freeze dell'esempio `pointer`). Nel testo consegnato la nota dice
solo che i contributi si elidono, e `sec:pointer` non parla del ronzio.

Lettura della knowledge base (non nel paper): il sistema non è mai trasparente nemmeno al grado
zero — coerente con la postura per cui ogni specifica è già un atto di
granulazione, e con la linea Keller-Rolfe → [[decorrelazione-granulare]]
(l'artefatto che la teoria DSP scarta diventa parametro compositivo).

## Sezioni del paper CIM 2026 dove usare

- **`sec:c-e`** (nota): finestrare il grano ne modula l'ampiezza aggiungendo bande laterali (Roads 2001); a sovrapposizione 2 si elidono.
- **`sec:completo`**: la finestra come inviluppo (Hann → `rexpodec` → Bartlett), leggibile nella testa del grano.

## Pagine collegate

[[time-stretching-granulare]] · [[decorrelazione-granulare]] ·
[[keller-rolfe1998]] · [[dutilleux2016]] · [[depoli-piccialli1988]] ·
[[roads2001-ch03-granular-synthesis]]
