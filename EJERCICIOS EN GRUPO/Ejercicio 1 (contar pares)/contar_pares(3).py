from concurrent.futures import ThreadPoolExecutor # Importamos ThreadPoolExecutor, para lanzar varias tareas en paralelo usando hilos.

def contar_pares_sublista(sublista):
    return sum(1 for x in sublista if x % 2 == 0)

def contar_pares(a):
    n = len(a) # tamaño de la lista 
    num_threads = 4 # usamos 4 hilos
    size = n // num_threads # tamaño de cada sublista 
    sublistas = [a[i:i+size] for i in range(0, n, size)] # partimos la lista en trozos de size 
    # Ejemplo: Si a tiene 20 elementos y num_threads=4, size=5, y habrá 4 sublistas de 5 elementos cada una. 

    with ThreadPoolExecutor() as executor:
        resultados = executor.map(contar_pares_sublista, sublistas)
        # executor.map(función, lista_de_datos) ejecuta la función contar_pares_sublista en paralelo para cada sublista.

    return sum(resultados) # Cada hilo devuelve el número de pares de su sublista

# arreglo de ejemplo 
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Lista:", a)
print("Cantidad de números pares:", contar_pares(a))