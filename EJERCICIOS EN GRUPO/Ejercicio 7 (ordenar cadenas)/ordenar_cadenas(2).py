def ordenar_cadena_insercion(cadena):
    # Convertimos la cadena a una lista de caracteres para poder intercambiar
    lista = list(cadena)
    
    # Recorremos desde el segundo elemento hasta el final
    for i in range(1, len(lista)):
        clave = lista[i]  # Guardamos el carácter actual
        j = i - 1
        
        # Movemos los elementos mayores que 'clave' una posición adelante
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        
        lista[j + 1] = clave  # Insertamos 'clave' en su posición correcta
    
    # Convertimos de nuevo a cadena
    return ''.join(lista)

# Ejemplo
print(ordenar_cadena_insercion("hola"))  # Resultado: "ahlo"
