# EJERCICIO 1:Contar números pares en una lista

def contar_pares(a):
    contador = 0
    for numero in a:
        if numero % 2 == 0:  # Si es divisible entre 2, es par
            contador += 1
    return contador

# arreglo de ejemplo 
a = [1, 2, 3, 4, 5, 6, 8, 9, 10]
print(contar_pares(a))
