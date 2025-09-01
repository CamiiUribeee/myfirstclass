import random

def quickselect(arr, k):
    """
    Encuentra el k-ésimo elemento más pequeño en arr (k empieza en 1).
    """
    if len(arr) == 1:
        return arr[0]
    
    # Elegimos un pivote aleatorio
    pivot = random.choice(arr)
    
    # Particionamos el arreglo
    menores = [x for x in arr if x < pivot]
    iguales = [x for x in arr if x == pivot]
    mayores = [x for x in arr if x > pivot]
    
    if k <= len(menores):
        return quickselect(menores, k)
    elif k <= len(menores) + len(iguales):
        return pivot
    else:
        return quickselect(mayores, k - len(menores) - len(iguales))

# Ejemplo:
arr = [7, 10, 4, 3, 20, 15]
k = 5
resultado = quickselect(arr, k)
print(f"El {k}-ésimo elemento más pequeño es: {resultado}")
