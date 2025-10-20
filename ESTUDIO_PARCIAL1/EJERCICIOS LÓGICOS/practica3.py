def esPalindromo_T(n):
    nuevoString=str(n)
    return nuevoString==nuevoString[::-1]

numeros=[121,123,43,565]

for num in numeros:
    if esPalindromo_T(num):
        print(f"el numero {num} es palindromo")
    else:
        print(f"el numero {num} no es palindromo")