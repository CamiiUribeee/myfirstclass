def busqueda_lineal_enumerate(a, objetivo):
    """
    Busca un elemento en la lista usando enumerate.
    Retorna el índice si lo encuentra, o -1 si no está.
    Complejidad:
      - Mejor caso: O(1) (si está al inicio)
      - Peor caso: O(n) (si no está o está al final)
    """
    for indice, valor in enumerate(a):
        if valor == objetivo:
            return indice  # Retorna el índice donde lo encontró
    return -1  # No encontrado

a = [10, 23, 45, 70, 11, 15]
print(busqueda_lineal_enumerate(a, 70))  
print(busqueda_lineal_enumerate(a, 28)) 