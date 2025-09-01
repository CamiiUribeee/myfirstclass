def son_anagramas_sort(palabra1, palabra2):
    if len(palabra1) != len(palabra2):
        return False
    return sorted(palabra1) == sorted(palabra2)

# Ejemplo:
print(son_anagramas_sort("hola", "aloh"))  # True
print(son_anagramas_sort("hola", "halo"))  # True 
