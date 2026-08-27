# Costo del rendering — dove vive la misura

**La documentazione completa non sta qui: sta nel repository di PGE**,
`docs/explanation/costo-rendering.md` (branch `docs/costo-rendering`,
2026-08-27). Questa pagina registra solo perché la misura è stata fatta, cosa ha
cambiato nel paper, e i numeri che servono a chi lavora sul testo.

## Perché è stata fatta

Punto C1 della review interna
(`raw/reviews/claude-review-claims-2026-08-26.md`): la `\notaRepo` di
`sec:architettura` affermava che «il costo di calcolo non cresce con la durata
d'ascolto ma col numero di grani», senza una misura.

**Il claim era falso come assoluto.** A numero di grani costante e durata
crescente il tempo cresce: il buffer di uscita va allocato, normalizzato e
scritto. Il modello vero ha due termini,

```
t = a · N_grani + b · D_secondi      a ≈ 32 µs/grano, b ≈ 1,3 ms/s
```

che pareggiano attorno ai **40 grani al secondo**. Il regime granulare d'uso sta
sopra quella soglia (Roads, *Microsound* p. 106: 50-100 g/s è già banda
continua), quindi il claim resta vero *nel regime in cui si lavora* — ed è così
che il paper ora lo formula, senza numeri.

Dato collaterale utile al paper: su materiale reale (`configs/PGE_cim.yml`,
994 291 grani su 92,5 s, 28,9 s totali) **circa un terzo del tempo è costruire
gli oggetti `Grain`**, non il DSP. È il prezzo della rappresentazione intermedia
esplicita, cioè della cosa che rende possibili la `map` e gli export. Se servisse
un aggancio argomentativo in `sec:architettura`, è questo.

## Cosa dice il paper adesso

`\notaRepo` non porta più formula, coefficienti né caso concreto — decisione
dell'autore del 2026-08-27: quei dettagli appesantivano una nota che parla
d'altro. Resta una frase, con il rinvio alla documentazione del progetto:

> Alle densità d'uso il costo del rendering è governato dal numero di grani, non
> dalla durata del pezzo; la misura è documentata nel repository.

Lo script di benchmark e il target `make bench` **non stanno più nel repo del
paper**: vivono in PGE (`utils/bench_cost.py`, `make bench [YAML=<file>]`), dove
misurano il motore invece del paper. Il submodule resta pinnato a v8.0.0, che non
li contiene: per rilanciarli si usa il repo PGE di lavoro.

## Vedi anche

- `docs/explanation/costo-rendering.md` in PGE — modello, ripartizione delle
  fasi, trade-off sequenziale/parallelo e lazy/eager, memoria per grano
- [[numpy-audio-renderer]] — overlap-add e path parallelo
