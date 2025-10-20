def esPrimo_T(n):
    if n <= 1:
        return False 
    
    for i in range(2,n):
        if n % i ==0:
            return False
    return True 

def contarPrimos_T(a,b):
    contador=0
    for num in range(a,b+1):
        if esPrimo_T(num):
            contador+=1
    return contador

intervalos=[(1,10), (25,50), (1,100)]
for a,b in intervalos:
    print(f"intervalos [{a}, {b}] -> {contarPrimos_T(a,b)} primos")

