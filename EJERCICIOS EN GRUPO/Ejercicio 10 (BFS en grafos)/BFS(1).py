from collections import deque

def bfs(graph, start):
    visited = set()         # Para no visitar nodos repetidos
    queue = deque([start])  # Cola para BFS
    order = []              # Lista para guardar el orden de visita

    while queue:
        node = queue.popleft()  # Sacamos el primer nodo
        if node not in visited:
            visited.add(node)
            order.append(node)
            
            # Agregar vecinos no visitados a la cola
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return order

# Ejemplo de uso
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(bfs(graph, 'A'))
