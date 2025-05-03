def parse_graph_file(filepath):
    """
    Lit un fichier de graphe et renvoie deux tableaux distincts.
    :param filepath: Chemin du fichier contenant le graphe
    :return: Deux tableaux (matrices) de taille spécifiée dans le fichier
    """
    with open(filepath, 'r') as file:
        lines = file.readlines()

    # La première ligne contient la taille du graphe
    n = int(lines[0].strip())

    # Les lignes suivantes contiennent les deux tableaux
    matrix_1 = []
    matrix_2 = []

    # Parcourir les lignes restantes pour remplir les deux matrices
    for i in range(n):
        matrix_1.append(list(map(int, lines[1 + i].strip().split())))
    for i in range(n):
        matrix_2.append(list(map(int, lines[1 + n + i].strip().split())))

    return matrix_1, matrix_2

#==========================================================================


import math
from functions_max_flow import ford_fulkerson, push_relabel
def bellman_ford(graph, cost, source, sink):
    """
    Algorithme de Bellman-Ford pour trouver le plus court chemin en coût.
    :param graph: Matrice de capacité résiduelle
    :param cost: Matrice de coûts
    :param source: Noeud source
    :param sink: Noeud puits
    :return: (distance, parent) pour reconstruire le chemin
    """
    n = len(graph)
    distance = [math.inf] * n
    parent = [-1] * n
    distance[source] = 0

    for _ in range(n - 1):
        for u in range(n):
            for v in range(n):
                if graph[u][v] > 0 and distance[u] + cost[u][v] < distance[v]:
                    distance[v] = distance[u] + cost[u][v]
                    parent[v] = u

    return distance, parent


def min_cost_max_flow(graph, cost, source, sink):
    """
    Implémente le flot maximum à coût minimal avec Bellman-Ford.
    :param graph: Matrice de capacités
    :param cost: Matrice des coûts
    :param source: Noeud source
    :param sink: Noeud puits
    :return: (flot total, coût total)
    """
    n = len(graph)
    flow = 0
    min_cost = 0

    # Créer une copie de la matrice pour travailler avec le graphe résiduel
    residual = [row[:] for row in graph]

    while True:
        distance, parent = bellman_ford(residual, cost, source, sink)

        if distance[sink] == math.inf:
            break  # Aucun chemin de coût minimal restant

        # Déterminer le flot possible (bottleneck)
        increment = math.inf
        v = sink
        while v != source:
            u = parent[v]
            increment = min(increment, residual[u][v])
            v = u

        # Appliquer le flot
        v = sink
        while v != source:
            u = parent[v]
            residual[u][v] -= increment
            residual[v][u] += increment  # arc retour
            min_cost += increment * cost[u][v]
            v = u

        flow += increment

    return flow, min_cost





# Exemple d'utilisation
if __name__ == "__main__":
    filepath = "graphs/graph8.txt"  # Remplacez par le chemin de votre fichier
    matrix_1, matrix_2 = parse_graph_file(filepath)

    print("Matrice 1 :")
    for row in matrix_1:
        print(row)

    print("\nMatrice 2 :")
    for row in matrix_2:
        print(row)

    source = 0
    sink = 5
    target_flow = ford_fulkerson(matrix_1, source, sink)[0]
    print(f"\nFlot cible : {target_flow}")

    flow, total_cost = min_cost_max_flow(matrix_1, matrix_2, source, sink)

    print(f"Flot maximum : {flow}")
    print(f"Coût minimal : {total_cost}")
    print("Matrice des flots :")
