import random
import time
import sys
from collections import defaultdict, deque

def generar_dag_aleatorio(n, densidad=0.1):
    """
    Genera un grafo dirigido acíclico (DAG) aleatorio con n vértices.
    """
    grafo = defaultdict(list)
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < densidad:
                grafo[i].append(j)
    return grafo

def topological_sort(grafo):
    """
    Realiza ordenamiento topológico en un DAG.
    Retorna: orden, comparaciones, 'intercambios' (nodos procesados).
    """
    comparaciones = 0
    intercambios = 0

    # Calcular los grados de entrada
    in_degree = {u: 0 for u in grafo}
    for u in grafo:
        for v in grafo[u]:
            in_degree[v] = in_degree.get(v, 0) + 1
            comparaciones += 1  # contar como comparación/actualización

    # Cola para vértices con grado de entrada 0
    cola = deque([u for u in grafo if in_degree[u] == 0])

    orden = []
    while cola:
        u = cola.popleft()
        orden.append(u)
        intercambios += 1  # cada nodo extraído cuenta como un intercambio lógico

        for v in grafo[u]:
            in_degree[v] -= 1
            comparaciones += 1
            if in_degree[v] == 0:
                cola.append(v)

    return orden, comparaciones, intercambios


def main():
    n = 100
    print("=" * 60)
    print("DAG - TOPOLOGICAL SORT - ANÁLISIS DE RENDIMIENTO")
    print("=" * 60)
    print(f"Elementos (n): {n}")
    print()

    grafo = generar_dag_aleatorio(n)
    memoria_grafo = sys.getsizeof(grafo) / 1024.0

    inicio = time.perf_counter()
    orden, comparaciones, intercambios = topological_sort(grafo)
    fin = time.perf_counter()

    tiempo_ms = (fin - inicio) * 1000

    print("RESULTADOS:")
    print("-" * 50)
    print(f"✓ Tiempo de ejecución: {tiempo_ms:.4f} ms")
    print(f"✓ Comparaciones: {comparaciones}")
    print(f"✓ Intercambios (procesos de nodos): {intercambios}")
    print(f"✓ Memoria del grafo: {memoria_grafo:.2f} KB")
    print()
    print("INFORMACIÓN ADICIONAL:")
    print("-" * 50)
    print(f"Complejidad temporal: O(V + E)")
    print(f"Complejidad espacial: O(V + E)")
    print(f"Número de vértices procesados: {len(orden)}")
    print()
    print("Primeros 10 nodos en orden topológico:", orden[:10])
    print("=" * 60)


if __name__ == "__main__":
    main()
