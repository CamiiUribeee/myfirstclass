def busqueda_lineal(a, objetivo):
    """
    Busca un elemento en la lista.
    Retorna el índice si lo encuentra, o -1 si no está.
    """
    for i in range(len(a)):
        if a[i] == objetivo:
            return i  # Retorna el índice si encuentra el objetivo
    return -1  # No encontrado

# Ejemplo de uso
a = [10, 23, 45, 70, 11, 15]
print(busqueda_lineal(a, 70))