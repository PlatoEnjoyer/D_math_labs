import itertools

def create_adjacency_set(edges, num_vertices=10):
    """Создает множество ребер"""
    adj_set = set()
    for u, v in edges:
        adj_set.add((u, v))
        adj_set.add((v, u))
    return adj_set

def check_isomorphism(edges1, edges2, num_vertices=10):
    """
    Проверяет изоморфизм графов полным перебором всех биекций
    Возвращает (True, isomorphism) если изоморфны, иначе (False, None)
    """
    adj1 = create_adjacency_set(edges1, num_vertices)
    adj2 = create_adjacency_set(edges2, num_vertices)
    
    vertices = list(range(num_vertices))
    
    for perm in itertools.permutations(vertices):
        is_isomorphism = True
        
        for u in range(num_vertices):
            for v in range(u + 1, num_vertices):
                # Проверяем ребро (u,v) в G1
                edge_in_g1 = (u, v) in adj1
                # Проверяем ребро (f(u), f(v)) в G2
                edge_in_g2 = (perm[u], perm[v]) in adj2
                
                if edge_in_g1 != edge_in_g2:
                    is_isomorphism = False
                    break
            if not is_isomorphism:
                break
        
        if is_isomorphism:
            return True, perm
    
    return False, None

edges1 = [
    (0, 1), (0, 3), (1, 2), (1, 5), (1, 7), (1, 8),
    (2, 3), (2, 7), (2, 8), (2, 9), (3, 4), (3, 5),
    (3, 6), (3, 9), (4, 5), (4, 6), (4, 8), (5, 6),
    (5, 9), (6, 7), (6, 8), (7, 8), (7, 9), (8, 9)
]

edges2 = [
    (0, 2), (0, 3), (0, 5), (0, 7), (0, 8), (0, 9),
    (1, 4), (1, 7), (2, 4), (2, 6), (2, 8), (3, 4),
    (3, 5), (3, 7), (3, 9), (4, 5), (4, 6), (4, 8),
    (5, 6), (5, 9), (6, 7), (6, 8), (7, 9), (8, 9)
]

is_iso, mapping = check_isomorphism(edges1, edges2)

if is_iso:
    print("Графы изоморфны")
    print("\nНайденный изоморфизм f: G1 -> G2")
    print("Вершина в G1 -> Вершина в G2")
    for i in range(10):
        print(f"    {i} -> {mapping[i]}")
else:
    print("Графы не изоморфны")