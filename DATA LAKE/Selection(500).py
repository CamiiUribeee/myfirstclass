import random
import time
import sys

def selection_sort(arr):
    """
    Implementación de Selection Sort con métricas
    Retorna: comparaciones, intercambios
    """
    comparaciones = 0
    intercambios = 0
    n = len(arr)
    
    for i in range(n - 1):
        # Encontrar el índice del elemento mínimo
        min_idx = i
        
        for j in range(i + 1, n):
            comparaciones += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Intercambiar el elemento mínimo con el primero
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            intercambios += 1
    
    return comparaciones, intercambios

def main():
    # Configuración
    n = 500
    print("=" * 50)
    print("SELECTION SORT - ANÁLISIS DE RENDIMIENTO")
    print("=" * 50)
    print(f"Elementos (n): {n}")
    print()
    
    # Generar array aleatorio
    array = [random.randint(0, 1000) for _ in range(n)]
    
    # Memoria del array (en KB)
    memoria_array = sys.getsizeof(array) / 1024.0
    
    # Medir tiempo de ejecución
    tiempo_inicio = time.perf_counter()
    comparaciones, intercambios = selection_sort(array)
    tiempo_fin = time.perf_counter()
    
    # Calcular tiempo en milisegundos
    tiempo_ms = (tiempo_fin - tiempo_inicio) * 1000
    
    # Memoria usada adicional (siempre será 0 para algoritmos in-place)
    memoria_adicional = 0.0  # Selection Sort no usa memoria extra
    
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
    print("COMPARACIÓN CON n=100:")
    print(f"  • Comparaciones esperadas: {500*499//2} (n×(n-1)/2)")
    print(f"  • Factor de crecimiento: {(500**2)/(100**2)}x")
    print(f"  • Intercambios: mucho menos que Insertion Sort")
    print()
    print("Primeros 10 elementos ordenados:", array[:10])
    print("Últimos 10 elementos ordenados:", array[-10:])
    print("=" * 50)

if __name__ == "__main__":
    main()