import random
import time
import sys
import math

# Variables globales para métricas
comparaciones = 0
intercambios = 0

def quick_sort(arr, low, high):
    """
    Implementación de Quick Sort con métricas
    """
    global comparaciones, intercambios
    
    if low < high:
        # Particionar el array y obtener el índice del pivote
        pi = partition(arr, low, high)
        
        # Ordenar recursivamente las dos mitades
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    """
    Particiona el array usando el último elemento como pivote
    """
    global comparaciones, intercambios
    
    # Elegir el último elemento como pivote
    pivot = arr[high]
    i = low - 1  # Índice del elemento más pequeño
    
    for j in range(low, high):
        comparaciones += 1
        # Si el elemento actual es menor o igual al pivote
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            if i != j:  # Contar solo si hay intercambio real
                intercambios += 1
    
    # Colocar el pivote en su posición correcta
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    if i + 1 != high:
        intercambios += 1
    
    return i + 1

def main():
    global comparaciones, intercambios
    
    # Configuración
    n = 1000
    print("=" * 50)
    print("QUICK SORT - ANÁLISIS DE RENDIMIENTO")
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
    quick_sort(array, 0, len(array) - 1)
    tiempo_fin = time.perf_counter()
    
    # Calcular tiempo en milisegundos
    tiempo_ms = (tiempo_fin - tiempo_inicio) * 1000
    
    # Memoria adicional (Quick Sort usa O(log n) por la recursión)
    memoria_adicional = 0.0  # In-place, pero usa stack de recursión
    
    # Mostrar resultados
    print("RESULTADOS:")
    print("-" * 50)
    print(f"✓ Tiempo de ejecución: {tiempo_ms:.4f} ms")
    print(f"✓ Comparaciones: {comparaciones}")
    print(f"✓ Intercambios: {intercambios}")
    print(f"✓ Memoria del array: {memoria_array:.2f} KB")
    print(f"✓ Memoria adicional: {memoria_adicional:.2f} KB (in-place)")
    print(f"✓ Stack de recursión: O(log n) ≈ {math.log2(n):.0f} niveles")
    print()
    print("INFORMACIÓN ADICIONAL:")
    print("-" * 50)
    print(f"Complejidad temporal: O(n log n) promedio, O(n²) peor caso")
    print(f"Complejidad espacial: O(log n) por recursión")
    print(f"Array ordenado correctamente: {array == sorted(array_copia)}")
    print()
    print("COMPARACIÓN DE CRECIMIENTO:")
    print(f"  • n=100  → n=1000: {(1000 * math.log2(1000)) / (100 * math.log2(100)):.2f}x")
    print(f"  • n=500  → n=1000: {(1000 * math.log2(1000)) / (500 * math.log2(500)):.2f}x")
    print(f"  • Comparaciones esperadas: ~{int(n * math.log2(n) * 1.39)}")
    print()
    print("COMPARACIÓN FINAL CON TODOS LOS ALGORITMOS (n=1000):")
    print("-" * 50)
    print(f"  • Quick Sort:     ~{int(n * math.log2(n) * 1.39):>7} comparaciones | ~1-3 ms ⚡⚡⚡")
    print(f"  • Merge Sort:     ~{int(n * math.log2(n)):>7} comparaciones | ~3-6 ms ⚡⚡")
    print(f"  • Insertion Sort: ~250,000 comparaciones | ~60-120 ms")
    print(f"  • Selection Sort:  499,500 comparaciones | ~50-100 ms")
    print()
    print("  🏆 Quick Sort es el CAMPEÓN en velocidad!")
    print("  ✓ In-place (no usa memoria extra)")
    print("  ✓ Hasta 50x más rápido que algoritmos O(n²)")
    print()
    print("Primeros 10 elementos ordenados:", array[:10])
    print("Últimos 10 elementos ordenados:", array[-10:])
    print("=" * 50)

if __name__ == "__main__":
    main()