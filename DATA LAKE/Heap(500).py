import random
import time
import sys
import math

# Variables globales para métricas
comparaciones = 0
intercambios = 0

def heapify(arr, n, i):
    """
    Convierte un subárbol con raíz en el índice i en un max-heap
    n es el tamaño del heap
    """
    global comparaciones, intercambios
    
    largest = i  # Inicializar el más grande como raíz
    left = 2 * i + 1  # Hijo izquierdo
    right = 2 * i + 2  # Hijo derecho
    
    # Ver si el hijo izquierdo existe y es mayor que la raíz
    if left < n:
        comparaciones += 1
        if arr[left] > arr[largest]:
            largest = left
    
    # Ver si el hijo derecho existe y es mayor que el más grande actual
    if right < n:
        comparaciones += 1
        if arr[right] > arr[largest]:
            largest = right
    
    # Cambiar la raíz si es necesario
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        intercambios += 1
        
        # Recursivamente heapify el subárbol afectado
        heapify(arr, n, largest)

def heap_sort(arr):
    """
    Implementación de Heap Sort con métricas
    """
    global comparaciones, intercambios
    
    n = len(arr)
    
    # Construir un max heap
    # Empezar desde el último nodo padre hasta la raíz
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extraer elementos uno por uno del heap
    for i in range(n - 1, 0, -1):
        # Mover la raíz actual (el más grande) al final
        arr[0], arr[i] = arr[i], arr[0]
        intercambios += 1
        
        # Llamar heapify en el heap reducido
        heapify(arr, i, 0)

def main():
    global comparaciones, intercambios
    
    # Configuración
    n = 500
    print("=" * 50)
    print("HEAP SORT - ANÁLISIS DE RENDIMIENTO")
    print("=" * 50)
    print(f"Elementos (n): {n}")
    print()
    
    # Generar array aleatorio
    array = [random.randint(0, 1000) for _ in range(n)]
    array_copia = array.copy()
    
    # Memoria del array (en KB)
    memoria_array = sys.getsizeof(array) / 1024.0
    
    # Resetear contadores
    comparaciones = 0
    intercambios = 0
    
    # Medir tiempo de ejecución
    tiempo_inicio = time.perf_counter()
    heap_sort(array)
    tiempo_fin = time.perf_counter()
    
    # Calcular tiempo en milisegundos
    tiempo_ms = (tiempo_fin - tiempo_inicio) * 1000
    
    # Memoria adicional (Heap Sort es in-place)
    memoria_adicional = 0.0
    
    # Mostrar resultados
    print("RESULTADOS:")
    print("-" * 50)
    print(f"✓ Tiempo de ejecución: {tiempo_ms:.4f} ms")
    print(f"✓ Comparaciones: {comparaciones}")
    print(f"✓ Intercambios: {intercambios}")
    print(f"✓ Memoria del array: {memoria_array:.2f} KB")
    print(f"✓ Memoria adicional usada: {memoria_adicional:.2f} KB (in-place)")
    print()
    print("INFORMACIÓN ADICIONAL:")
    print("-" * 50)
    print(f"Complejidad temporal: O(n log n) en todos los casos")
    print(f"Complejidad espacial: O(1)")
    print(f"Array ordenado correctamente: {array == sorted(array_copia)}")
    print()
    print("COMPARACIÓN CON n=100:")
    print(f"  • Comparaciones esperadas: ~{int(2 * n * math.log2(n))} (≈2n log₂ n)")
    print(f"  • Factor de crecimiento: ~{(500 * math.log2(500)) / (100 * math.log2(100)):.2f}x")
    print()
    print("COMPARACIÓN CON OTROS ALGORITMOS (n=500):")
    print(f"  • Quick Sort:  ~6,200 comp. | ~0.5-1 ms ⚡⚡⚡")
    print(f"  • Merge Sort:  ~4,483 comp. | ~1-2 ms ⚡⚡")
    print(f"  • Heap Sort:   ~{int(2 * n * math.log2(n))} comp. | ~1-3 ms ⚡⚡")
    print(f"  • Insertion:  ~62,500 comp. | ~12-20 ms")
    print(f"  • Selection: 124,750 comp. | ~12-25 ms")
    print(f"  • Bubble:     ~62,500 comp. | ~50-100 ms")
    print()
    print("Primeros 10 elementos ordenados:", array[:10])
    print("Últimos 10 elementos ordenados:", array[-10:])
    print("=" * 50)

if __name__ == "__main__":
    main()