from collections import Counter

def son_anagramas(palabra1, palabra2):
    # Si tienen diferente longitud, no son anagramas
    if len(palabra1) != len(palabra2):
        return False
    
    # Contar frecuencias de letras en cada palabra
    contador1 = Counter(palabra1) # Counter para contar cuántas veces aparece cada letra en cada palabra
    contador2 = Counter(palabra2)
    
    # Comparar diccionarios
    return contador1 == contador2

# Pruebas
print(son_anagramas("roma", "amor"))  # True
print(son_anagramas("hola", "halo"))  # True # porque tienen las mismas letras en la misma cantidad
print(son_anagramas("perro", "ropa")) # False
