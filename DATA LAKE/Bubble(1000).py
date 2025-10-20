import random
import time
import sys

def bubble_sort(arr):
    """
    Implementación de Bubble Sort con métricas
    Retorna: comparaciones, intercambios
    """
    comparaciones = 0
    intercambios = 0
    n = len(arr)
    
    # Recorrer todos los elementos
    for i in range(n):
        # Flag para optimización (detectar si ya está ordenado)
        swapped = False
        
        # Los últimos i elementos ya están en su lugar
        for j in range(0, n - i - 1):
            comparaciones += 1
            # Intercambiar si el elemento actual es mayor que el siguiente
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambios += 1
                swapped = True
        
        # Si no hubo intercambios, el array ya está ordenado
        if not swapped:
            break
    
    return comparaciones, intercambios

def main():
    # Configuración
    n = 1000
    print("=" * 50)
    print("BUBBLE SORT - ANÁLISIS DE RENDIMIENTO")
    print("=" * 50)
    print(f"Elementos (n): {n}")
    print()
    
    # Generar array aleatorio
    array = [random.randint(0, 1000) for _ in range(n)]
    
    # Memoria del array (en KB)
    memoria_array = sys.getsizeof(array) / 1024.0
    
    # Medir tiempo de ejecución
    tiempo_inicio = time.perf_counter()
    comparaciones, intercambios = bubble_sort(array)
    tiempo_fin = time.perf_counter()
    
    # Calcular tiempo en milisegundos
    tiempo_ms = (tiempo_fin - tiempo_inicio) * 1000
    
    # Memoria usada adicional (siempre será 0 para algoritmos in-place)
    memoria_adicional = 0.0  # Bubble Sort no usa memoria extra
    
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
    print(f"Complejidad temporal: O(n²)")
    print(f"Complejidad espacial: O(1)")
    print(f"Array ordenado correctamente: {array == sorted(array)}")
    print()
    print("COMPARACIÓN DE CRECIMIENTO:")
    print(f"  • n=100  → n=1000: {(1000**2)/(100**2)}x más operaciones")
    print(f"  • n=500  → n=1000: {(1000**2)/(500**2)}x más operaciones")
    print(f"  • Comparaciones máximas: {1000*999//2}")
    print()
    print("TABLA COMPARATIVA FINAL - TODOS LOS ALGORITMOS (n=1000):")
    print("-" * 50)
    print(f"  🥇 Quick Sort:     ~13,800 comp. | ~1-3 ms")
    print(f"  🥈 Merge Sort:      ~9,966 comp. | ~3-6 ms")
    print(f"  🥉 Insertion Sort: ~250,000 comp. | ~60-120 ms")
    print(f"  4️⃣  Selection Sort: 499,500 comp. | ~50-100 ms")
    print(f"  🐌 Bubble Sort:    ~250,000 comp. | ~200-400 ms ⚠️")
    print()
    print("  Bubble Sort es hasta 100-200x MÁS LENTO que Quick Sort!")
    print("  Por eso casi nunca se usa en producción.")
    print()
    print("Primeros 10 elementos ordenados:", array[:10])
    print("Últimos 10 elementos ordenados:", array[-10:])
    print("=" * 50)

if __name__ == "__main__":
    main()