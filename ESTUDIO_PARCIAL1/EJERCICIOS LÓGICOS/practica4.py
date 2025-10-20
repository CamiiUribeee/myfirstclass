def esPerfecto_T(n):
    if n <=1:
        return False
    
    c=1
    for i in range(2,n):
        if n%i ==0:
            c+=i
    return c==n

numeros=[28,496,5]

for num in numeros:
    if esPerfecto_T(num):
        print(f"el numero {num} es perfecto")
    else:
        print(f"el numero {num} no es perfecto")