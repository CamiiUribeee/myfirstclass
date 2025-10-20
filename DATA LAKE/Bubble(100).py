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
    n = 100
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
    print("CARACTERÍSTICAS DE BUBBLE SORT:")
    print("  • Algoritmo más simple de entender")
    print("  • Estable (mantiene orden relativo)")
    print("  • Comparaciones máximas: n(n-1)/2")
    print("  • Con optimización: detecta arrays ordenados")
    print("  • Generalmente el más lento de todos")
    print()
    print("Primeros 10 elementos ordenados:", array[:10])
    print("Últimos 10 elementos ordenados:", array[-10:])
    print("=" * 50)

if __name__ == "__main__":
    main()