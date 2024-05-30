#### Timeline

- **17.05**: 
  - Funktionierende simple Lösung (Brute Force) \
  - Eine Sprache
  - In der Sprache für verschiedene Knotenzahlen prüfen, ab wann es kaputtgeht \
  - Konkrete Werte Benchmark


- **24.04**:
  - Andere Sprachen - Jeder macht eigene Lösung
  - Optimierte(re) Lösung?
  - Visualisierung?

  
#### Beispiel Haus vom Nikolaus

**Darstellung Knoten** \
       KN1


KN2           KN3




KN4           KN5


**Darstellung als Adjazenzmatrix** \
    1 2 3 4 5
kn1 0 1 1 0 0 \
kn2 _ 0 1 1 1 \
kn3 _ _ 0 1 1 \
kn4 _ _ _ 0 1 \
kn5 _ _ _ _ 0 \

**Darstellung als Wort**
Nikolaus haus = 1100111111

    kn1 kn2 kn3 kn4 kn5
kn1  
kn2
kn3
kn4
kn5

Word Array:
[['1', '1', '0', '0'], ['1', '1', '1'], ['1', '1'], ['1']]