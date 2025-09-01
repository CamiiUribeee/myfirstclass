def sumar_matriz(matriz):
    total = 0  # Inicializamos la suma en 0
    for fila in matriz:  # Recorremos cada fila
        for elemento in fila:  # Recorremos cada elemento de la fila
            total += elemento  # Sumamos cada elemento al total
    return total
    
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(sumar_matriz(matriz)) 