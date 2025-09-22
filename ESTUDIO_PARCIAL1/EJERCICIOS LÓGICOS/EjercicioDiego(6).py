#Determinar la suma en una lista de numeros 

def suma_numeros(lista):
    total=0
    for num in lista:
        total+=num
    return total

n=int(input("Ingrese la cantidad de numeros: "))
numeros=list(map(int, input("Ingresa los numeros separado por un espacio cada uno: ").split()))

print("La suma es: ", suma_numeros(numeros))

#Complejidad algorítimica: O(n)