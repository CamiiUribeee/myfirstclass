import random
import time
import sys

def bellman_ford(graph, source):
    """
    Implementación de Bellman-Ford con métricas.
    Retorna: distancias, comparaciones, actualizaciones.
    """
    n = len(graph)
    dist = [float('inf')] * n
    dist[source] = 0
    comparaciones = 0
    actualizaciones = 0

    for _ in range(n - 1):
        for u in range(n):
            for v, peso in graph[u]:
                comparaciones += 1
                if dist[u] + peso < dist[v]:
                    dist[v] = dist[u] + peso
                    actualizaciones += 1

    return dist, comparaciones, actualizaciones


def generar_grafo_aleatorio(n, densidad=0.2):
    """Genera un grafo dirigido aleatorio con pesos positivos."""
    graph = [[] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if u != v and random.random() < densidad:
                peso = random.randint(1, 20)
                graph[u].append((v, peso))
    return graph


def main():
    n = 500
    print("=" * 60)
    print("BELLMAN-FORD - ANÁLISIS DE RENDIMIENTO")
    print("=" * 60)
    print(f"Número de vértices (n): {n}")
    print()

    graph = generar_grafo_aleatorio(n)
    memoria_grafo = sys.getsizeof(graph) / 1024.0

    inicio = time.perf_counter()
    distancias, comparaciones, actualizaciones = bellman_ford(graph, 0)
    fin = time.perf_counter()

    tiempo_ms = (fin - inicio) * 1000

    print("RESULTADOS:")
    print("-" * 50)
    print(f"✓ Tiempo de ejecución: {tiempo_ms:.4f} ms")
    print(f"✓ Comparaciones: {comparaciones}")
    print(f"✓ Actualizaciones (intercambios): {actualizaciones}")
    print(f"✓ Memoria del grafo: {memoria_grafo:.2f} KB")
    print(f"✓ Complejidad temporal: O(V * E)")
    print(f"✓ Complejidad espacial: O(V)")
    print()
    print("Ejemplo de distancias desde el vértice 0 (primeros 10):")
    print(distancias[:10])
    print("=" * 60)


if __name__ == "__main__":
    main()
