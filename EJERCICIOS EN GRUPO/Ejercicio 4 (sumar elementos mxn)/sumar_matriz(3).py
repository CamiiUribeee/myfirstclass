def suma_matriz_divide_venceras(matriz, fila_inicio, fila_fin, col_inicio, col_fin):
    # Caso base: si la submatriz es de un solo elemento
    if fila_inicio == fila_fin and col_inicio == col_fin:
        return matriz[fila_inicio][col_inicio]

    # Si hay solo una fila, recorrer columnas
    if fila_inicio == fila_fin:
        return sum(matriz[fila_inicio][col_inicio:col_fin + 1])

    # Si hay solo una columna, recorrer filas
    if col_inicio == col_fin:
        return sum(matriz[i][col_inicio] for i in range(fila_inicio, fila_fin + 1))

    # Dividir en 4 submatrices
    fila_media = (fila_inicio + fila_fin) // 2
    col_media = (col_inicio + col_fin) // 2

    suma1 = suma_matriz_divide_venceras(matriz, fila_inicio, fila_media, col_inicio, col_media)
    suma2 = suma_matriz_divide_venceras(matriz, fila_inicio, fila_media, col_media + 1, col_fin)
    suma3 = suma_matriz_divide_venceras(matriz, fila_media + 1, fila_fin, col_inicio, col_media)
    suma4 = suma_matriz_divide_venceras(matriz, fila_media + 1, fila_fin, col_media + 1, col_fin)

    return suma1 + suma2 + suma3 + suma4


# Ejemplo
matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

resultado = suma_matriz_divide_venceras(matriz, 0, len(matriz)-1, 0, len(matriz[0])-1)
print(f"Suma de todos los elementos: {resultado}")
