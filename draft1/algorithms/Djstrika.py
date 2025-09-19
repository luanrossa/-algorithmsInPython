import heapq  # Biblioteca para usar fila de prioridade (mínimo custo sempre no topo)

def dijkstra(grafo, inicio):
    """
    Implementação do algoritmo de Dijkstra para encontrar
    a menor distância de um nó inicial até todos os outros nós de um grafo.
    
    :param grafo: dicionário onde as chaves são nós e os valores são listas de tuplas (vizinho, peso)
    :param inicio: nó de origem
    :return: distâncias mínimas do nó inicial até cada nó
    """
    
    # Dicionário que armazenará a distância mínima conhecida até cada nó
    distancias = {no: float('inf') for no in grafo}
    distancias[inicio] = 0  # A distância do nó inicial para ele mesmo é 0
    
    # Fila de prioridade para escolher sempre o próximo nó com menor distância
    fila = [(0, inicio)]  # (distância, nó)
    
    while fila:
        # Extrai o nó com menor distância acumulada até agora
        distancia_atual, no_atual = heapq.heappop(fila)
        
        # Se já encontramos um caminho melhor antes, ignoramos este
        if distancia_atual > distancias[no_atual]:
            continue
        
        # Explora os vizinhos do nó atual
        for vizinho, peso in grafo[no_atual]:
            distancia = distancia_atual + peso  # custo acumulado
            
            # Se encontramos um caminho mais curto até o vizinho, atualizamos
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                # Coloca na fila para explorar futuramente
                heapq.heappush(fila, (distancia, vizinho))
    
    return distancias


# ================== EXEMPLO DE USO ==================

# Grafo representado como lista de adjacências
# Cada chave é um nó, e o valor é uma lista de (vizinho, peso)
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

inicio = 'A'
resultado = dijkstra(grafo, inicio)

print("Menores distâncias a partir do nó", inicio)
for no, distancia in resultado.items():
    print(f"{inicio} -> {no} = {distancia}")
