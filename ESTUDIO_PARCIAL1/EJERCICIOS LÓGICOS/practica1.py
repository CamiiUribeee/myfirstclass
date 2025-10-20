def esPrimo_T(n):
    if n <= 1:
        return False 
    
    for i in range(2,n):
        if n % i ==0:
            return False 
    return True 

N=int(input("Escriba un número: "))
if esPrimo_T(N):
    print(f"el número {N} es primo")
else:
    print(f"el número {N} no es primo")