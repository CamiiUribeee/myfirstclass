import random
import time
import sys

def bellman_ford(grafo, n, inicio):
    """
    Implementación del algoritmo de Bellman-Ford con métricas.
    Retorna: distancias, comparaciones, intercambios
    - comparaciones: cada intento de relajación de una arista
    - intercambios: cuando una distancia mejora
    """
    dist = [float('inf')] * n
    dist[inicio] = 0

    comparaciones = 0
    intercambios = 0

    # Relajar todas las aristas n-1 veces
    for _ in range(n - 1):
        for u, v, peso in grafo:
            comparaciones += 1
            if dist[u] + peso < dist[v]:
                dist[v] = dist[u] + peso
                intercambios += 1

    # Verificar ciclos negativos (solo comparaciones)
    for u, v, peso in grafo:
        comparaciones += 1
        if dist[u] + peso < dist[v]:
            print("⚠️ Ciclo negativo detectado.")
            break

    return dist, comparaciones, intercambios


def generar_grafo(n, densidad=0.05, peso_max=20):
    """
    Genera una lista de aristas (u, v, peso) para un grafo dirigido.
    """
    grafo = []
    for i in range(n):
        for j in range(n):
            if i != j and random.random() < densidad:
                peso = random.randint(-5, peso_max)  # permite pesos negativos
                grafo.append((i, j, peso))
    return grafo


def main():
    n = 100
    print("=" * 60)
    print("ALGORITMO DE BELLMAN-FORD - ANÁLISIS DE RENDIMIENTO")
    print("=" * 60)
    print(f"Nodos (n): {n}\n")

    # Generar grafo aleatorio
    grafo = generar_grafo(n)
    inicio = random.randint(0, n - 1)

    # Calcular memoria del grafo
    memoria_grafo = sys.getsizeof(grafo) / 1024.0
    memoria_adicional_estimada = (sys.getsizeof([0]*n)) / 1024.0

    # Ejecutar algoritmo
    tiempo_inicio = time.perf_counter()
    distancias, comparaciones, intercambios = bellman_ford(grafo, n, inicio)
    tiempo_fin = time.perf_counter()

    tiempo_ms = (tiempo_fin - tiempo_inicio) * 1000

    # Mostrar resultados
    print("RESULTADOS:")
    print("-" * 60)
    print(f"✓ Nodo inicial: {inicio}")
    print(f"✓ Tiempo de ejecución: {tiempo_ms:.4f} ms")
    print(f"✓ Comparaciones (relajaciones): {comparaciones}")
    print(f"✓ Intercambios (actualizaciones de distancia): {intercambios}")
    print(f"✓ Memoria del grafo: {memoria_grafo:.2f} KB")
    print(f"✓ Memoria adicional estimada: {memoria_adicional_estimada:.2f} KB (distancias)")
    print()
    print("INFORMACIÓN ADICIONAL:")
    print("-" * 60)
    print(f"Complejidad temporal: O(V * E)")
    print(f"Complejidad espacial: O(V)")
    print(f"Ejemplo de distancias desde el nodo {inicio}: {distancias[:10]}")
    print()
    print("CARACTERÍSTICAS DE BELLMAN-FORD:")
    print("  • Calcula las rutas más cortas desde un nodo origen.")
    print("  • Soporta pesos negativos (a diferencia de Dijkstra).")
    print("  • Detecta ciclos negativos en el grafo.")
    print("  • Más lento que Dijkstra en grafos grandes.")
    print("=" * 60)


if __name__ == "__main__":
    main()
