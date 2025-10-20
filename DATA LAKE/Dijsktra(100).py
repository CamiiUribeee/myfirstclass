import random
import time
import sys
import heapq

def dijkstra(grafo, inicio):
    """
    Implementación del algoritmo de Dijkstra con métricas.
    Retorna: distancias mínimas, comparaciones (int), intercambios (int)
    - comparaciones: intento de relajar una arista (se evalúa la condición).
    - intercambios: número de push al heap (actualizaciones efectivas/pendientes).
    """
    n = len(grafo)
    dist = [float('inf')] * n
    dist[inicio] = 0
    visitado = [False] * n
    heap = [(0, inicio)]  # (distancia, nodo)

    comparaciones = 0
    intercambios = 0

    while heap:
        d_actual, u = heapq.heappop(heap)
        if visitado[u]:
            continue
        visitado[u] = True

        for v, peso in grafo[u]:
            comparaciones += 1  # evaluamos si dist[u] + peso < dist[v]
            if dist[u] + peso < dist[v]:
                dist[v] = dist[u] + peso
                heapq.heappush(heap, (dist[v], v))
                intercambios += 1  # contamos el push como "intercambio"

    return dist, comparaciones, intercambios


def generar_grafo(n, densidad=0.1, peso_max=20):
    """
    Genera un grafo aleatorio con n nodos y cierta densidad de aristas.
    Representación: lista de adyacencia, cada entrada es (vecino, peso).
    """
    grafo = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and random.random() < densidad:
                peso = random.randint(1, peso_max)
                grafo[i].append((j, peso))
    return grafo


def main():
    n = 100  # Número de nodos
    print("=" * 60)
    print("ALGORITMO DE DIJKSTRA - ANÁLISIS DE RENDIMIENTO")
    print("=" * 60)
    print(f"Nodos (n): {n}\n")

    # Generar grafo aleatorio
    grafo = generar_grafo(n)

    # Medir memoria del grafo (estimada) en KB
    memoria_grafo = sys.getsizeof(grafo) / 1024.0

    # Estimar memoria adicional: dist list + heap (vacío inicial)
    memoria_adicional_estimada = (sys.getsizeof([0]*n) + sys.getsizeof([])) / 1024.0

    # Ejecutar Dijkstra
    inicio = random.randint(0, n - 1)
    tiempo_inicio = time.perf_counter()
    distancias, comparaciones, intercambios = dijkstra(grafo, inicio)
    tiempo_fin = time.perf_counter()

    # Calcular tiempo en milisegundos
    tiempo_ms = (tiempo_fin - tiempo_inicio) * 1000

    # Resultados
    print("RESULTADOS:")
    print("-" * 60)
    print(f"✓ Nodo inicial: {inicio}")
    print(f"✓ Tiempo de ejecución: {tiempo_ms:.4f} ms")
    print(f"✓ Comparaciones (intentos de relajación): {comparaciones}")
    print(f"✓ Intercambios (push al heap): {intercambios}")
    print(f"✓ Memoria del grafo: {memoria_grafo:.2f} KB")
    print(f"✓ Memoria adicional estimada: {memoria_adicional_estimada:.2f} KB (dist + heap)")
    print()
    print("INFORMACIÓN ADICIONAL:")
    print("-" * 60)
    print(f"Complejidad temporal: O((V + E) log V)")
    print(f"Complejidad espacial: O(V)")
    print(f"Ejemplo de distancias desde el nodo {inicio}: {distancias[:10]}")
    print()
    print("CARACTERÍSTICAS DE DIJKSTRA:")
    print("  • Calcula rutas más cortas desde un nodo origen.")
    print("  • Utiliza una cola de prioridad (heap) para eficiencia.")
    print("  • No funciona con pesos negativos.")
    print("  • Muy usado en redes, GPS y optimización de rutas.")
    print("=" * 60)


if __name__ == "__main__":
    main()
