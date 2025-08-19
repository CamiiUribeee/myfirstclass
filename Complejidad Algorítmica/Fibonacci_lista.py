def fibonacci_lista(n):
    sucesion = [0, 1]                  # O(1) → lista inicial con los 2 primeros
    for i in range(2, n+1):            # O(n) → recorre desde el 2 hasta n
        sucesion.append(sucesion[i-1] + sucesion[i-2])  # O(1) por iteración
    return sucesion[:n+1]              # O(n) → devuelve los primeros n+1 elementos

# Programa principal
num = 10                               # O(1)
resultado = fibonacci_lista(num)       # O(n)
print("Sucesión de Fibonacci hasta", num, "es:", resultado)  # O(n)
