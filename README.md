# Libreria clasic cuantum    
##cuantum 
en esta libreria se plantearon funciones basicas de la 
fisica cuantica, asi como el resolver de algunos ejercicios dados
de el libro

donde estos fueron representados y hechos en python 
asi como en este readme, tambien se va a tener la discusion
de 2 ejercicios .


##Descripción y contexto
###SIMULE EL PRIMER SISTEMA CUÁNTICO DESCRITO EN LA SECCIÓN 4.1.

1. El sistema debe calcular la probabilidad de encontrarlo 
   en una posición en particular.
   
2. El sistema si se le da otro vector Ket debe buscar la probabilidad 
   de transitar del primer vector al segundo.
   
###COMPLETE LOS RETOS DE PROGRAMACIÓN DEL CAPÍTULO 4

1. Ahora con una matriz que describa un observable y un 
   vector ket, el sistema revisa que la matriz sea hermitiana, y si lo es, calcula la media 
   y la varianza del observable en el estado dado.
   
2. El sistema calcula los valores propios del observable y la probabilidad de que el sistema transite 
   a alguno de los vectores propios después de la observación.

3. Se considera la dinámica del sistema. Ahora con una serie de matrices Un el sistema 
calcula el estado final a partir de un estado inicial

###REALICE LOS SIGUIENTES PROBLEMAS E INCLUYALOS COMO EJEMPLOS
Modele en su librería los problemas

4.3.1

4.4.1

4.4.2
***
##discusión de los ejercicios 4.5.2 y 4.5.3

4.5.2: como ya sebemos un poco de la fisica cuantica sabemos que para hallar los spins
lo que se debe hacer es tener la norma del vector y la probabilidad de que este arriba o abajo
pero se tiene que saber todos los estados posible que puede tener, ara poder generalizar y no 
solo tenerlo en lo de ejercicios de fue de 2x2 si no que podria resolver ejercicios de nxn

4.5.3 como vimos en la clase si es un estado separable, ya que este se puede representar como
producto tensor de dos estados individuales, no estan entrelasados, significa que una particula puede
estar en otro estados, y no importa el estado de la particula que estabamos calculando,
tmbien como se vio en la clase se ve que esta tiene infinitas soluciones y puede ser ya numeros
enteros como tambien numeros imaginarios.

##modelos de los problemas del libro

* en  ese se saco la probabilidad de que podria tener el spin y cuando es arriba y cuantos veces era
que este se podia rhacer, entonces la solucion, fue sacar la probabilidad para la veces que se
  podia
  
* en este problema usando la libreria de numpy se solucion muy rapido porque con dos comandos
basicos numpy me puede sacar la transpuesta conjugada y de una vez me multiplica para saber,
  si son unitaria o no, y con esto pudimos verificar que todas eran matrices heritianas
  
* en este problema como muchos en la libreria anteriores calculamos la posibilidad, de que se encontrara
en un estado haciendo la multiplicacion, y la elevada al cuadrado, igual se multiplico con la
  ayuda de la libreria de numpy
## Aclaraciones
***

1. la libreria basic cuantum solo representa los problemas dados y se creo un main donde al 
   correrlo da la soluciones de los problemas modulas y su solucion, las otras funciones solo 
   se crearon pero no tienen prueba 
2. en las funciones para hacer falta la primera de la segunda parte porque no upe bien como
representarla.
   
3. en la libreria esta documentado todo para que sea mas facil la lectura y comprension del
trabajo realisado

   
## Autor/es
***
* autor: SANTIAGO OSPINA MEJIA 

* apoyo/ aportes: LUIS DANIEL BENAVIDES NAVARRO
          
