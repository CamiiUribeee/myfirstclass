import random
import time
import sys
import math

# Variables globales para métricas
comparaciones = 0
intercambios = 0

def merge_sort(arr):
    """
    Implementación de Merge Sort con métricas
    """
    global comparaciones, intercambios
    
    if len(arr) <= 1:
        return arr
    
    # Dividir el array en dos mitades
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Combinar las dos mitades ordenadas
    return merge(left, right)

def merge(left, right):
    """
    Combina dos arrays ordenados en uno solo
    """
    global comparaciones, intercambios
    
    result = []
    i = j = 0
    
    # Comparar elementos y combinar
    while i < len(left) and j < len(right):
        comparaciones += 1
        if left[i] <= right[j]:
            result.append(left[i])
            intercambios += 1
            i += 1
        else:
            result.append(right[j])
            intercambios += 1
            j += 1
    
    # Agregar elementos restantes
    while i < len(left):
        result.append(left[i])
        intercambios += 1
        i += 1
    
    while j < len(right):
        result.append(right[j])
        intercambios += 1
        j += 1
    
    return result

def main():
    global comparaciones, intercambios
    
    # Configuración
    n = 500
    print("=" * 50)
    print("MERGE SORT - ANÁLISIS DE RENDIMIENTO")
    print("=" * 50)
    print(f"Elementos (n): {n}")
    print()
    
    # Generar array aleatorio
    array = [random.randint(0, 1000) for _ in range(n)]
    array_original = array.copy()
    
    # Memoria del array original (en KB)
    memoria_array = sys.getsizeof(array) / 1024.0
    
    # Resetear contadores
    comparaciones = 0
    intercambios = 0
    
    # Medir tiempo de ejecución
    tiempo_inicio = time.perf_counter()
    array_ordenado = merge_sort(array)
    tiempo_fin = time.perf_counter()
    
    # Calcular tiempo en milisegundos
    tiempo_ms = (tiempo_fin - tiempo_inicio) * 1000
    
    # Memoria adicional (Merge Sort usa O(n) de espacio extra)
    memoria_adicional = sys.getsizeof(array_ordenado) / 1024.0
    
    # Mostrar resultados
    print("RESULTADOS:")
    print("-" * 50)
    print(f"✓ Tiempo de ejecución: {tiempo_ms:.4f} ms")
    print(f"✓ Comparaciones: {comparaciones}")
    print(f"✓ Intercambios (movimientos): {intercambios}")
    print(f"✓ Memoria del array: {memoria_array:.2f} KB")
    print(f"✓ Memoria adicional usada: {memoria_adicional:.2f} KB")
    print()
    print("INFORMACIÓN ADICIONAL:")
    print("-" * 50)
    print(f"Complejidad temporal: O(n log n)")
    print(f"Complejidad espacial: O(n)")
    print(f"Array ordenado correctamente: {array_ordenado == sorted(array_original)}")
    print()
    print("COMPARACIÓN CON n=100:")
    print(f"  • Comparaciones esperadas: ~{int(n * math.log2(n))} (n log₂ n)")
    print(f"  • Factor de crecimiento: ~{(500 * math.log2(500)) / (100 * math.log2(100)):.2f}x")
    print()
    print("COMPARACIÓN CON OTROS ALGORITMOS (n=500):")
    print(f"  • Merge Sort: ~{int(n * math.log2(n))} comparaciones")
    print(f"  • Selection Sort: 124,750 comparaciones")
    print(f"  • Insertion Sort: ~62,500 comparaciones")
    print(f"  • Merge es MUCHO más eficiente!")
    print()
    print("Primeros 10 elementos ordenados:", array_ordenado[:10])
    print("Últimos 10 elementos ordenados:", array_ordenado[-10:])
    print("=" * 50)

if __name__ == "__main__":
    main()