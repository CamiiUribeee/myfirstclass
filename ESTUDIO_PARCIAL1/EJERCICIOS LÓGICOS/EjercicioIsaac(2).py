#determinar cantidad de numeros primos en un intervalo en especifico
def esPrimo_T(n):
    if n<=1:
        return False
    
    for i in range(2,n):
        if n%i==0:
            return False
    return True 
    
def contar_primos_T(a,b):
    c=0
    for num in range(a,b+1):
        if esPrimo_T(num):
            c+=1
    return c

intervalos=[(1,20), (1,100), (1,50)]
for a,b in intervalos:
    print(f"Intervalo [{a}, {b}] -> {contar_primos_T(a,b)} primos")

        
#complejidad algoritmica O(n) en el peor de los casos