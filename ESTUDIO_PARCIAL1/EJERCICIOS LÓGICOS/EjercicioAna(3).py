#determinar si la representación decimal de un número es palíndromo
def esPalindromo_T(n):
    nuevoString=str(n)
    return nuevoString==nuevoString[::-1]

numeros=[1001, 121, 131, 234]

for num in numeros:
    if esPalindromo_T(num):
        print("Es palindromo")
    else:
        print("No es palindromo")

#Complejidad algoritmica es O(logn)