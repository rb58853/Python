

# Proyecto II de DAA

### Nombres
- Rául Beltrán Gómez C412
- Mauricio Mamud Sánchez C412

---- 

## Problema:

Se da la tarea de encontrar el mejor subgrafo tal que la suma de los pesos de las aristas menos los de los vértices sea la mayor posible.

---

## Solución usando Flujo:

Se crea un grafo G' dirigido a partir del grafo original G. G' tiene un vértice $s$ y $t$ (source y sink del flujo), ademas cada una de las aristas de G serán representadas en G' por por un vértice ($a_i$), también cada uno de los vértices de G en G' estarán representados con un vértice ($v_i$). Luego se conectan $s$ con cada uno de los $a_i$ y se le da una capacidad asociada al peso de la arista que representa $a_i$ en G. Luego cada $a_i$ está conectado a 2 $v_{is}$ los cuales representan los vertices de la arista en cuestión, esta arista de  conexión en G' tiene capacidad $\infin$. Por úlitmo en la construcción del G', se conecta cada $v_i$ con $t$ teniendo esta conexión una capacidad igual al peso del vertice asociado en G.

Se aplica un algoritmo de mincut-maxflow como por ejemplo Edmonds-Karp, tomando el source y el sink como $s$ y $t$ respectivamente.

Luego nos quedamos con el flujo en las aristas de G' que van de las $v_i$ a $t$ tal que no estén saturadas. Se removen del grafo original los vertices asociados a estas aristas. 

Se retorna el valor del subgrafo restante de G sin estos vertices y se da como solución.

### Correctitud
Podemos reformular el problema, asumamos que tenemos toda la ganancia que brindan las aristas de G, si no logramos con esta ganacia satisfacer la perdida que dan los vertices asociados a cada una de estas, entonces no es posible incluir ese vertice en el subgrafo solución y por ende todas sus aristas.

Creando G' se puede modelar lo anterior usando un algoritmo de flujo, miraremos nuestro corte mínimo, si se corta algún arco entre $s$ y algún $a_i$ entonces se incluiría el uso de la ganancia de la arista asociada a $a_i$ en G, si se corta algún arco entre la $a_i$ y $v_j$, entonces se tiene que satisfacer la perdida del j-esimo vertice, se puede ver que si se incluye una arista de G entonces se tienen que incluir sus vertices asociados en G o sacar la arista de la solución pues sería imposible cortar el arco de peso $\infin$ entre ellos en G'.

Luego si no se satura alguna arista de G' desde $v_i$ a $t$ implicaría que no se puede satisfacer la perdida que genera por lo que el vertice de G asociado $v_i$ no se debe incluir en la solución.

### Complejidad temporal
Depende del algoritmo de flujo usado, en este caso usamos Edmons-Karp el cual tiene una complejidad de $O(VE^2)$, dado que construimos un grafo adicional, donde la cantidad de los vertices es |V'| = |E| + |V| + 2 y |E'|=|V|+|E|+2|E| = |V|+3|E|. Luego la complejidad es $O((|V|+|E|)*(|V|+3|E|)^2)$  que sería al final $O((|V|+|E|)^3)$ .