import random
import time
import sys
from collections import deque

def generar_grafo(n, densidad=0.05):
    """
    Genera un grafo no dirigido aleatorio con n nodos.
    densidad controla la cantidad de aristas (entre 0 y 1).
    """
    grafo = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < densidad:
                grafo[i].append(j)
                grafo[j].append(i)
    return grafo

def bfs(grafo, inicio):
    """
    Implementación de BFS con métricas.
    Retorna: comparaciones, intercambios, nodos visitados
    """
    visitado = set()
    cola = deque([inicio])
    visitado.add(inicio)

    comparaciones = 0
    intercambios = 0

    while cola:
        nodo = cola.popleft()
        for vecino in grafo[nodo]:
            comparaciones += 1
            if vecino not in visitado:
                visitado.add(vecino)
                cola.append(vecino)
                intercambios += 1

    return comparaciones, intercambios, len(visitado)

def main():
    # Configuración
    n = 500
    print("=" * 60)
    print("BFS (Breadth-First Search) - ANÁLISIS DE RENDIMIENTO")
    print("=" * 60)
    print(f"Nodos (n): {n}\n")

    # Generar grafo aleatorio
    grafo = generar_grafo(n)

    # Medir memoria base (en KB)
    memoria_grafo = sys.getsizeof(grafo) / 1024.0

    # Medir tiempo de ejecución
    tiempo_inicio = time.perf_counter()
    comparaciones, intercambios, visitados = bfs(grafo, 0)
    tiempo_fin = time.perf_counter()

    # Calcular métricas
    tiempo_ms = (tiempo_fin - tiempo_inicio) * 1000
    memoria_adicional = (sys.getsizeof(set()) + sys.getsizeof(deque())) / 1024.0

    # Mostrar resultados
    print("RESULTADOS:")
    print("-" * 60)
    print(f"✓ Tiempo de ejecución: {tiempo_ms:.4f} ms")
    print(f"✓ Comparaciones: {comparaciones}")
    print(f"✓ Intercambios: {intercambios}")
    print(f"✓ Nodos visitados: {visitados}")
    print(f"✓ Memoria del grafo: {memoria_grafo:.2f} KB")
    print(f"✓ Memoria adicional usada: {memoria_adicional:.2f} KB\n")

    print("INFORMACIÓN ADICIONAL:")
    print("-" * 60)
    print("Complejidad temporal: O(V + E)")
    print("Complejidad espacial: O(V)")
    print(f"Recorrido completo: {'Sí' if visitados == n else 'Parcial'}\n")

    print("CARACTERÍSTICAS DE BFS:")
    print("  • Recorre el grafo por niveles (amplitud).")
    print("  • Usa una cola para almacenar nodos pendientes.")
    print("  • Encuentra el camino más corto (en número de aristas).")
    print("  • Se usa en búsquedas, grafos, juegos, redes, etc.")
    print("=" * 60)

if __name__ == "__main__":
    main()
