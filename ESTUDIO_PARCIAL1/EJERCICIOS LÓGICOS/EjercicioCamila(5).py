#Determinar el numero de prefectos en un intervalo dado 

import math
def esPerfecto_T(a,b):
    contador=0
    for num in range(a,b+1):
        raiz=int(math.sqrt(num))
        if raiz*raiz == num:
            contador+=1
    return contador

intervalos=[(1,10), (5,20), (30,40)]
for a,b in intervalos:
    print(f"intervalos [{a}, {b}] -> {esPerfecto_T(a,b)} números perfectos")

#Complejidad algorítmica O(n) en el peor de los casos 