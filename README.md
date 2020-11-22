
# Sterowanie w labiryncie heksagonalnym:
 Z racji tego, że z każdej z komórek może być maksymalnie 6 dróg wyjścia, to w labiryncie poruszamy się za pomocą sekwencji 2 odczytów z klawiatury (strzałki)
 
 To znaczy, że jeśli chcemy przejść do komórki znajdującej się na prawo od aktualnej pozycji to 2 razy klikamy →
 
 ##__Wszystkie możliwości:__
 * __NE__ : → + ↑ lub ↑ + →
 * __E__ : → + →
 * __SE__ : → + ↓ lub ↓ + →
 * __SW__ : ← + ↓ lub ↓ + ←
 * __W__ : ← + ←
 * __NW__ : ← + ↑ lub ↑ + ←





# Project_Labyrinth
## Ogólny zamysł:
> ### Naszym projektem jest generowanie labiryntu jednym, lub w późniejszej fazie kilkoma, algorytmami i przedstawienie tego w interfejsie graficznym
> Tak jak na [tym filmie](https://youtu.be/6kv5HKPB1XU  "Maze-film")
>
> Przykłady algów generujących: https://en.wikipedia.org/wiki/Maze_generation_algorithm
> 
> Później będziemy implementować algorytmy przeszukiwania tego labiryntu z ich graficznymi wizualizacjami 
> 
> Algi takie jak np.: 
> * BFS
> * DFS
> * A*
> * Dijkstra
> * https://en.wikipedia.org/wiki/Maze_solving_algorithm


Gist:
[Kod generacyjny labirynt heksagonalny za pomocą algorytmu DFS](https://gist.github.com/Aszman/e69a89f9e6ad39e182a9f5537de0ebac)
