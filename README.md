# practica2algoritmia


GREEDY -Iterativo Como el objetivo es calcular el menor coste de punto a punto antes de añadirlo al acumulador, debemos hacer ese cálculo en todos los puntos del perfil terrestre. Con el primer bucle lo que hacemos es situarnos en el último punto en el cual hayamos construido el pilar con el menor coste. Mientras que con el bucle interior es con el que buscamos cual es el punto más óptimo hasta el que construir la siguiente plataforma. -Recursivo Nuestro final de recursividad es cuando estamos situados en el último punto del perfil terrestre, donde debe acabar el conducto a construir. Entonces, una vez en esta situación, simplemente devolvemos el coste acumulado. Sin embargo, si no estamos en el final del acueducto, debemos seguir calculando los costes. De eso se hará cargo nuestro bucle, con el for nos moveremos entre los distintos puntos que haya desde el punto actual hasta el final. Y en cada uno de ellos calculará el coste, quedándose con el mínimo y añadiendolo al acumulador.

Backtracking -Iterativo Teniendo en mente el uso del stack, será necesario seleccionar la rama en la cual debemos iterar y calcular los costes de las distintas rutas. Esto lo haremos mediante el primer bucle, del cual solo saldremos una vez hechos todos los cálculos, o dicho de otra manera, cuando el stack con los puntos esté vacío. -Recursivo Nuestra elección para el caso simple es situarnos en la primera columna. Como es una columna que siempre deberemos poner hacemos el cálculo del resto de nodos y finalmente ponemos el primer pilar. Como todo algoritmo backtracking recursivo, es dentro del bucle donde se pone la llamada recursiva y la recursividad aparece en la función que calcula el coste. La función que nos hace la llamada recursiva es, a su vez y como se ha comentado, la que realiza la llamada recursiva. Esto es debido a que calculamos el coste individual de cada nodo y lo sumamos al siguiente y así sucesivamente hasta llegar al caso simple, el cual devuelve el coste mencionado anteriormente.

Dynamic Programming -Iterativo El primer bucle es el que nos va a seleccionar qué rama, partiendo del nodo inicial, es la que estamos calculando. Mientras que, con el segundo bucle, es con el que vamos a calcular los distintos costes y con el que vamos a ir guardando cual es el coste de cada uno de los nodos.

-Recursivo Nuestro código se compone de un caso simple por tal de hacer que finalice ese bucle y sigue la dinámica de su versión iterativa. Por otro lado, debemos añadir obligatoriamente el último pilar del acueducto. Una vez pasados estos condicionales viene el bucle, con el que nos movemos por los distintos caminos de cada nodo y calculamos sus costes.


Enlace a github:
https://github.com/VictorMateu/practica2algoritmia.git
