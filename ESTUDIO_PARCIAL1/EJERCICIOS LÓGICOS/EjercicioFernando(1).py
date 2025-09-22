#determinar si un numero es primo o no 
def esPrimo_T(n):
    if n <= 1:
        return False 
    for i in range(2,n):
        if n % i ==0:
            return False
    return True 
    
N=int(input("Ingrese un número: "))
if esPrimo_T(N):
    print("Es primo")
else:
    print("No es primo")

#complejidad algoritmica: O(n) en el peor de los casos 