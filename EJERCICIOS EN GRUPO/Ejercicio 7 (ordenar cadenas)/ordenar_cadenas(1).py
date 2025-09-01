def ordenar_cadena(cadena):
    # Convertimos la cadena a lista porque las cadenas son inmutables: "hola" → ['h', 'o', 'l', 'a'].
    lista = list(cadena)
    n = len(lista)

    # Bubble sort
    for i in range(n): # recorre n veces 
        for j in range(0, n - i - 1): # compara elementos
            if lista[j] > lista[j + 1]: # si están en orden incorrecto (el de la izquierda es mayor al de la derecha)
                # Intercambiamos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    # Convertimos de nuevo a string
    return "".join(lista)

# Ejemplo
print(ordenar_cadena("algoritmo"))  # agilmoort
