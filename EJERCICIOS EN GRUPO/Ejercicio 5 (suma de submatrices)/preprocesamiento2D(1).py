def build_prefix_sum(matrix):
    if not matrix or not matrix[0]: #aseguramos que la matriz no está vacía 
        return []
    
    m, n = len(matrix), len(matrix[0]) # n=numero de filas, m=numero de columnas 
    prefix = [[0] * (n + 1) for _ in range(m + 1)]  # creamos una matriz llena de ceros, +1 para simplificar índices
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            prefix[i][j] = (
                matrix[i-1][j-1] # esta formula suma el valor actual de la matriz original ...
                + prefix[i-1][j] # ...la suma acumulada de la fila anterior, 
                + prefix[i][j-1] # la suma acumulada de la columna anterior,
                - prefix[i-1][j-1] # y resta la intersección doble contada 
            )
    return prefix # retorna prefix que permite calcular cualquier suma de submatrices 

def sum_submatrix(prefix, x1, y1, x2, y2): # para calcular la suma de los elementos dentro de una submatriz definida por las esquinas
    # Ajustar +1 porque prefix tiene fila/columna extra
    x1 += 1
    y1 += 1
    x2 += 1
    y2 += 1
    
    return (
        prefix[x2][y2] # suma total hasta la esquina inferior derecha.
        - prefix[x1-1][y2] # resta la parte superior. 
        - prefix[x2][y1-1] # resta la parte izquierda.
        + prefix[x1-1][y1-1] # suma la intersección que fue restada dos veces.
    )

# Ejemplo de uso
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

prefix = build_prefix_sum(matrix)
print(sum_submatrix(prefix, 0, 0, 1, 1))  # Suma de submatriz [(0,0) -> (1,1)]
print(sum_submatrix(prefix, 1, 1, 2, 2))  # Suma de submatriz [(1,1) -> (2,2)]
