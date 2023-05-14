

# Proyecto II de DAA

### Nombres
- Rául Beltrán Gómez C412
- Mauricio Mamud Sánchez C412

---- 
# Problema:

Sea $G(v,e)$ un grafo ponderado en vértices y aristas. Se desea encontrar el subgrafo que maximice la sumatoria del peso de las aristas menos la sumatoria del peso de los vértices. Sujeto a la restricción de que si una arista pertenece al subgrafo solución entonces también pertenecen ambos vértices a los cuales está conectada.

---- 

# Solución Greedy

## Definiciones:

**weight_degree:** Sea $v$ un vértice que pertenece a un grafo $G$, el weight_degree de $v$ es igual a $\sum e.weight$ $\forall e$ que esté asociada al vértice $v$ en el grafo $G$.

**profit:** El profit de un Grafo $G$ es el resultado de $\sum e.weight - \sum v.weight$ $\forall v,e \in G$

**Subgrafo de costo negativo($Gn$):** $Gn$ es un subgrafo de costo negativo de $G$ si al eliminar las componentes de $Gn$(vértices y aristas) de $G$ resulta que el profit de $G$ aumenta, es decir el profit de las componentes de $Gn$ resulta en pérdida.

**Subgrafo de costo menos positivo($Gm$):** $Gm$ es un subgrafo de costo menos positivo si el profit de $Gm$ es mínimo teniendo en cuenta todas las aristas que pertenecen a cada vértice de $Gm$ y sus vértices. Nótese que $Gm$ no es directamente positivo dado que no se tienen en cuenta los vértices que se conectan a las aristas que pertenecen a $Gm$ y que a su vez (los vértices) no pertenecen a $Gm$.

**Grafo irreducible($Gi$):** Un grafo $Gm$ o $Gn$ se considera irreducible si no existe un subgrafo del mismo con menos profit que el grafo dado.

**Grafo Dependiente($Gv$):** Se dice que un grafo es dependiente de un vértice $v$ si este grafo siempre debe contener el vértice $v$ como vértice del mismo.

## **Demostraciones**

**El subgrafo irreducible de G con menor cardinalidad es potencialmente eliminable:** Por definición no hay subgrafo de $Gi$ con menor profit que el mismo, luego el profit de $Gi$ no está influenciado por un subgrafo del mismo. Para que $Gi$ no sea potencialmente eliminable entonces tiene que suceder que hay al menos un vértice de $Gi$ que pertenece a un subgrafo que sí es potencialmente eliminable y el resto de los vértices de $Gi$ no deban estar incluidos en dicho subgrafo. Si esto sucede entonces un subconjunto de $Gi$ hacen peor el supuesto potencialmente eliminable, pero el resto de este subgrafo $Gi$ hace peor ese subconjunto de $Gi$, luego la componente se hace más mala con el subconjunto que a su vez se hace más malo con el subgrafo completo, luego $Gi$ completamente pertenece a esta componente mala ya que al pertenecer en su totalidad disminuye el profit de la componente potencialmente eliminable supuesta. Se puede decir entonces que dondequiera que se agregue un subconjunto de $Gi$ para empeorar una componente el resto de $Gi$ va a empeorar lo que se empeoró dado que el subconjunto de $Gi$ tiene más profit de $Gi$ por definición de grafo irreducible.

Un grafo es **potencialmente eliminable** si al eliminar uno de sus vértices todo los demás al eliminarlos reducen el profit del grafo, eso sucede siempre en un grafo $Gi$, si tomas un vértice arbitrario de $Gi$ se puede asegurar que $Gi$ es de menor profit que el mismo por definición. Luego se puede considerar la componente $Gi$ como un solo vértice, ya que al eliminar cualquier vértice se asegura que eliminar el resto es mejor. Nótese que esto no pasa si no es irreducible dado que podría existir un conjunto del subgrafo con menor profit que el mismo. 

Un grafo que no posee ningun subgrafo potencialmente eliminable es optimo para el resultado del ejercicio. Notese que si esto sucede entonces para cualquier componente conexa que se elimine del grafo, el mismo pierde profit dado que no posee subgrafos que al ser eliminados mejoren el profit.

**Influenciado** se refiere a que un conjunto de vértices y aristas disminuyen el profit de un conjunto más grande, lo cual implica que este conjunto grande está disminuyendo su profit por un tercero, esto implica que no puede ser potencialmente reducible.

## Algoritmo Greedy

### Paso 1

**Se desean buscar subgrafos potenciales a eliminar. Demostremos que el siguiente algoritmo calcula el grafo irreducible de $Gv$ para un $v$ dado.**

- El grafo debe contener obligatoriamente al vértice $v$ por definición de $Gv$.
- Pseudoeliminamos el vértice $v$. Se está asumiendo que $v$ siempre pertenece al grafo, luego habría que dejar de contar con las componentes de $v$ ya que estamos buscando un subgrafo potencialmente eliminable. De esta forma se lleva un valor de profit del grafo que estamos buscando.
    
    **pseudoeliminación:** dejar de contar con las componentes de un vértice en un subgrafo que se analiza, de esa forma al pseudoeliminar un vértice los vértices adyacentes al mismo pierden *weight_degree* según la arista que se deje de analizar que parte del vértice dado.
    
- El objetivo es buscar un grafo potencialmente a eliminar donde siempre se encuentre el vértice $v$, luego tras pseudoeliminar el vértice $v$ se analizan sus adyacentes en $G$, sea $a$ adyacente de $v$, si ahora el peso de $a$ es mayor que su *weight_degree* entonces evidentemente $a$ va a disminuir el profit de $Gv$, por lo tanto $a$ debe pertenecer al subgrafo $Gv$ que estamos buscando. Luego se pseudoelimina $a$.
- Se regresa al `paso 2` pasándole el vértice $a$ como $v$. Este algoritmo se realiza a modo de BFS. mientras se encuentre un vértice potencialmente malo se repite el algoritmo. Nótese que el algoritmo a lo sumo recorre todas las aristas y vértices del grafo una sola vez, dado que se eliminan las aristas y vértices que ya se tomaron.

**Al terminar el algoritmo se garantiza que:**

- En cada paso el profit del grafo disminuye, por lo tanto el subgrafo final $Gv$ es irreducible. Tengamos en cuenta que es irreducible para el caso que se encuentra $v$ obligatoriamente en el mismo, lo cual es la definición de $Gv$.
- A lo sumo se visitan todas las aristas y vértices del grafo original. $O(|E|+|V|)$

### Paso 2

Aplicamos el `paso 1` y el algoritmo `reduce` a todos los vértices del grafo para calcular $Gv$ para cada $v$ que pertenece a $G$. De esta forma tendremos todos los subgrafos irreducibles de $G$ que dependen de un $v$ dado. Nótese que un subgrafo de $G$ debe siempre tener al menos un vértice, en este caso pasamos por cada $v$ y de esta manera tendremos todos los subgrafos asociados a cada $v$. Este algoritmo aplica el `paso 1` $|V|$ veces, luego es $O(|V| * (|V|+|E|))$.

### Paso 3

Una vez calculado el `paso 2` si encontramos un $Gv$ con profit negativo eliminamos el menor de los estos $Gv$ del grafo y repetimos el proceso del `paso 2`. Si no encontramos un $Gv$ con profit negativo mezclamos el $Gv$ de menor profit y cardinalidad mínima, priorizando la cardinalidad, es decir de los $Gv$ de mínima cardinalidad mezclamos el de menor profit. Esto último lo hacemos dado que $Gv$ es mínimo e irreducible y por la definición y demostración no viola nada realizar esta operación de mezcla. Dado que en cada iteración del `paso 2` se reduce el grafo a lo sumo se realiza este `paso 3` $v$ veces ya que este se repite mientras en `paso 2` se produzca un cambio, sobre la complejidad de reduce se explica en su apartado. Luego la complejidad del algoritmo es $O(V^2(|V|+|E|))$.

**mezcla:** Ahora todos los vértices del grafo $Gv$ serán un solo vértice (sea ese vértice $v$) con peso igual a la suma de los vértices menos la suma de las aristas de $Gv$, donde no se incluyen las aristas que salen de $Gv$, es decir las aristas que no tienen ambos vértices incluidos en $Gv$. Se mantienen las aristas salientes de cada vértice a sus respectivos vértices fuera del subgrafo, si desde un vértice externo se llega a más de un vértice de $Gv$ la arista aumenta el peso por cada vértice al que entre según el peso de cada subarista, es decir en vez de tener $n$ aristas desde un vértice externo hacia $v$, habrá una sola arista con peso igual a la suma de todas estas.

## Algoritmo Reduce:

Este algoritmo reduce el grafo en cardinalidad. Por cada arista si la arista es mayor que ambos pesos de los vértices que la contienen los vértices se mezclan dado que si un vértice se encuentra en la solución en otro vértice también se encontrará. Nótese que si un vértice pertenece al grafo solución entonces quedará el otro vértice suelto con un peso menor que el de la arista dada, entonces se debe agregar al grafo resultante porque aporta profit al mismo, luego el grafo solución no debe contener ambos. Este algoritmo se aplica a todas las aristas del grafo y mientras haya cambio se vuelve a aplicar. Por cada reducción el grafo se reduce, y eso implica que el `paso 2` que lo usa reduzca sus iteraciones, a lo sumo entre ambos algoritmos se pasará por todos los vértices del grafo haciendo operación en $O(|V|*(|V|+|E|))$. Esto garantiza que en el grafo nunca haya una arista de este tipo.

----

# Solución usando Flujo:

Se crea un grafo G' dirigido a partir del grafo original G. G' tiene un vértice $s$ y $t$ (source y sink del flujo), ademas cada una de las aristas de G serán representadas en G' por por un vértice ($a_i$), también cada uno de los vértices de G en G' estarán representados con un vértice ($v_i$). Luego se conectan $s$ con cada uno de los $a_i$ y se le da una capacidad asociada al peso de la arista que representa $a_i$ en G. Luego cada $a_i$ está conectado a 2 $v_{is}$ los cuales representan los vertices de la arista en cuestión, esta arista de  conexión en G' tiene capacidad $\infin$. Por úlitmo en la construcción del G', se conecta cada $v_i$ con $t$ teniendo esta conexión una capacidad igual al peso del vertice asociado en G.

Se aplica un algoritmo de mincut-maxflow como por ejemplo Edmonds-Karp, tomando el source y el sink como $s$ y $t$ respectivamente.

Luego nos quedamos con el flujo en las aristas de G' que van de las $v_i$ a $t$ tal que no estén saturadas. Se remueven del grafo original los vertices asociados a estas aristas.

Se retorna el valor del subgrafo restante de G sin estos vertices y se da como solución.

### Correctitud
Podemos reformular el problema, asumamos que tenemos toda la ganancia que brindan las aristas de G, si no logramos con esta ganacia satisfacer la perdida que dan los vertices asociados a cada una de estas, entonces no es posible incluir ese vertice en el subgrafo solución y por ende todas sus aristas.

Creando G' se puede modelar lo anterior usando un algoritmo de flujo, miraremos nuestro corte mínimo, si se corta algún arco entre $s$ y algún $a_i$ entonces se incluiría el uso de la ganancia de la arista asociada a $a_i$ en G, si se corta algún arco entre la $a_i$ y $v_j$, entonces se tiene que satisfacer la perdida del j-esimo vertice, se puede ver que si se incluye una arista de G entonces se tienen que incluir sus vertices asociados en G o sacar la arista de la solución pues sería imposible cortar el arco de peso $\infin$ entre ellos en G'.

Luego si no se satura alguna arista de G' desde $v_i$ a $t$ implicaría que no se puede satisfacer la perdida que genera por lo que el vertice de G asociado $v_i$ no se debe incluir en la solución.

### Complejidad temporal
Depende del algoritmo de flujo usado, en este caso usamos Edmons-Karp el cual tiene una complejidad de $O(VE^2)$, dado que construimos un grafo adicional, donde la cantidad de los vertices es |V'| = |E| + |V| + 2 y |E'|=|V|+|E|+2|E| = |V|+3|E|. Luego la complejidad es $O((|V|+|E|)*(|V|+3|E|)^2)$  que sería al final $O((|V|+|E|)^3)$ .
