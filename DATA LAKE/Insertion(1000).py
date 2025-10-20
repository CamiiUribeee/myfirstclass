import random
import time
import sys

def insertion_sort(arr):
    """
    Implementación de Insertion Sort con métricas
    Retorna: comparaciones, intercambios
    """
    comparaciones = 0
    intercambios = 0
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # Mover elementos mayores que key una posición adelante
        while j >= 0 and arr[j] > key:
            comparaciones += 1
            arr[j + 1] = arr[j]
            intercambios += 1
            j -= 1
        
        # Comparación final cuando sale del while
        if j >= 0:
            comparaciones += 1
        
        arr[j + 1] = key
    
    return comparaciones, intercambios

def main():
    # Configuración
    n = 1000
    print("=" * 50)
    print("INSERTION SORT - ANÁLISIS DE RENDIMIENTO")
    print("=" * 50)
    print(f"Elementos (n): {n}")
    print()
    
    # Generar array aleatorio
    array = [random.randint(0, 1000) for _ in range(n)]
    
    # Memoria del array (en KB)
    memoria_array = sys.getsizeof(array) / 1024.0
    
    # Medir tiempo de ejecución
    tiempo_inicio = time.perf_counter()
    comparaciones, intercambios = insertion_sort(array)
    tiempo_fin = time.perf_counter()
    
    # Calcular tiempo en milisegundos
    tiempo_ms = (tiempo_fin - tiempo_inicio) * 1000
    
    # Memoria usada adicional (siempre será 0 para algoritmos in-place)
    memoria_adicional = 0.0  # Insertion Sort no usa memoria extra
    
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
    print("COMPARACIÓN CON OTROS TAMAÑOS:")
    print(f"  • n=100  → n=1000: {(1000**2)/(100**2)}x más operaciones")
    print(f"  • n=500  → n=1000: {(1000**2)/(500**2)}x más operaciones")
    print(f"  • Factor cuadrático: O(n²)")
    print()
    print("Primeros 10 elementos ordenados:", array[:10])
    print("Últimos 10 elementos ordenados:", array[-10:])
    print("=" * 50)

if __name__ == "__main__":
    main()