def sumar_matriz_comprension(matriz):
    return sum(sum(fila) for fila in matriz)

# Ejemplo de uso
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 10]
]

resultado = sumar_matriz_comprension(matriz)
print("Suma de la matriz:", resultado)
