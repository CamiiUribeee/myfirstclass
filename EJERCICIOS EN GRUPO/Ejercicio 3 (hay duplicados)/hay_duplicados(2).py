def hay_duplicados(lista):
    """
    Determina si una lista contiene elementos duplicados.
    Complejidad: O(n²)
    """
    n = len(a)
    for i in range(n):  # Recorre cada elemento
        for j in range(i + 1, n):  # Compara con los siguientes
            if a[i] == a[j]:  # Si hay un duplicado
                return True
    return False

a = [1, 2, 3, 4, 5, 1]
print(hay_duplicados(a))  # True
