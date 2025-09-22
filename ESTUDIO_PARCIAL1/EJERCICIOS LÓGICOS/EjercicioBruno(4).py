#determinar si un numero es perfecto o no

def esPerfecto_T(n):
    if n<=1:
        return False
    
    c=1
    for i in range(2,n):
        if n%i==0:
            c+=i
    return c==n

numeros=[28,10,12,14]

for num in numeros:
    if esPerfecto_T(num):
        print(f"{num} -> Sí")
    else:
        print(f"{num} -> No")

#Complejidad algoritmica: O(n)