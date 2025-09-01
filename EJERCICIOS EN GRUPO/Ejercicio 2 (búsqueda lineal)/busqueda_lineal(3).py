from concurrent.futures import ThreadPoolExecutor

def buscar_chunk(a, objetivo, start, end):
    for i in range(start, end):
        if a[i] == objetivo:
            return i
    return -1

def busqueda_lineal_paralela(a, objetivo, num_threads=4):
    n = len(a)
    chunk_size = n // num_threads
    with ThreadPoolExecutor() as executor:
        futures = []
        for i in range(num_threads):
            start = i * chunk_size
            end = n if i == num_threads - 1 else (i+1) * chunk_size
            futures.append(executor.submit(buscar_chunk, a, objetivo, start, end))
        for f in futures:
            idx = f.result()
            if idx != -1:
                return idx
    return -1

# Ejemplo
a = [10, 23, 45, 70, 11, 15]
print(busqueda_lineal_paralela(a, 11))
