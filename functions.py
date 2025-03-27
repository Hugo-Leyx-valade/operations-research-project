from collections import deque
import copy


def graph_import(link):
    with open(link, 'r') as f:
        lines = f.readlines()
    graph = []  # Liste pour stocker le graphe
    # Lire et structurer les données du fichier
    type_of_problem =0
    if len(lines) >int(lines[0])+1:
        type_of_problem = 1
    else:
        type_of_problem = 2
    for line in lines[1:]:
        values = list(map(int, line.split()))  # fais un vecteur avec les valeurs de la ligne (1 1 => [1,1])
        graph.append(values)  # Stocker la ligne
    return (graph, type_of_problem)


def print_graph_to_matrix_of_values(liste_adjacence):
    # Déterminer la taille de la matrice
    n = len(liste_adjacence)
    # Créer une matrice remplie de '*'
    matrice = [['*' for _ in range(n)] for _ in range(n)]
    print("La matrice de capacité")
    # Remplir la matrice avec les valeurs données
    for i in range(n):
        for j in range(len(liste_adjacence[i])):
            matrice[i][j] = str(liste_adjacence[i][j])  # Stocker en tant que chaîne pour l'affichage
    # Affichage de l'en-tête des colonnes
    header = "    " + "  ".join(str(i) if i > 0 and i < n-1 else "s" if i == 0 else "t" for i in range(n))
    col_width = max(len(str(n)), 2)  # Largeur minimale de 2
    separator = "   " + "-" * (n * (col_width + 1))
    print(header)
    print(separator)
    # Affichage des lignes
    for i in range(n):
        row = f"{i if (i > 0 and i < n-1) else 's' if i == 0 else 't'} | " + "  ".join(matrice[i][j] if j < len(matrice[i]) else ' * ' for j in range(n))
        print(row)


import copy
from collections import deque

def ford_fulkerson(graph, s=0, t=None):
    n = len(graph)
    if t is None:
        t = n - 1  # si t non précisé, c'est le dernier sommet

    max_flow = 0
    residual = copy.deepcopy(graph)  # pour garder une copie du graphe résiduel

    iteration = 1
    while True:
        print(f"\n🌀 Itération {iteration} :")
        parent = [-1] * n
        flow, path = bfs(residual, s, t, parent)

        if flow == 0:
            print("❌ Aucun chemin améliorant trouvé. L'algorithme s'arrête.")
            break

        print(f"✔️ Chaîne améliorante trouvée : {' → '.join(map(str, path))}")
        print(f"🔁 Valeur de flot pour cette chaîne : {flow}")

        # Mise à jour du graphe résiduel
        u = t
        while u != s:
            v = parent[u]
            residual[v][u] -= flow
            residual[u][v] += flow
            u = v

        max_flow += flow

        print("📊 Graphe résiduel mis à jour :")
        print_graph_to_matrix_of_values(residual)

        iteration += 1

    print(f"\n🌊 Flot maximal trouvé : {max_flow}")
    return max_flow, residual



def bfs(residual, s, t, parent):
    n = len(residual)
    visited = [False] * n
    queue = deque([s])
    visited[s] = True

    while queue:
        u = queue.popleft()
        for v in range(n):
            if not visited[v] and residual[u][v] > 0:
                parent[v] = u
                visited[v] = True
                queue.append(v)
                if v == t:
                    # reconstruit le chemin
                    path = []
                    curr = t
                    while curr != -1:
                        path.append(curr)
                        curr = parent[curr]
                    path.reverse()
                    # calcule le flux minimal possible sur ce chemin
                    min_capacity = min(residual[parent[v]][v] for v in path[1:])
                    return min_capacity, path
    return 0, []

def print_graph_to_matrix_of_values(graph):
    for row in graph:
        print(" ".join(map(str, row)))



def print_flow_max(graph1, graph2):
    n = len(graph1)
    matrice = [['*' for _ in range(n)] for _ in range(n)]
    print("La matrice de capacité")
    # Remplir la matrice avec les valeurs données
    for i in range(n):
        for j in range(len(graph1[i])):
            matrice[i][j] = [[str(graph1[i][j] - graph2[i][j]) + '/' + str(graph1[i][j])]]
# Stocker en tant que chaîne pour l'affichage
    # Affichage de l'en-tête des colonnes
    header = "    " + "  ".join(str(i) if i > 0 and i < n - 1 else "s" if i == 0 else "t" for i in range(n))
    col_width = max(len(str(n)), 2)  # Largeur minimale de 2
    separator = "   " + "-" * (n * (col_width + 1))
    print(header)
    print(separator)
    # Affichage des lignes
    for i in range(n):
        row = f"{i if (i > 0 and i < n - 1) else 's' if i == 0 else 't'} | " + "  ".join(
            matrice[i][j] if j < len(matrice[i]) else ' * ' for j in range(n))
        print(row)

def compute_flow_matrix(original_graph, residual_graph):
    """ Calcule la matrice des flots maximaux """
    n = len(original_graph)
    # Créer une matrice remplie de '*'
    matrice = [['0' for _ in range(n)] for _ in range(n)]
    print("La matrice de capacité")
    # Remplir la matrice avec les valeurs données
    for i in range(n):
        for j in range(len(original_graph[i])):
            if original_graph[i][j] != 0:
                matrice[i][j] = str(original_graph[i][j] - residual_graph[i][j]) + '/' + str(original_graph[i][j])  # Stocker en tant que chaîne pour l'affichage
    



def print_graph(graph):
    """ Affiche proprement une matrice """
    for row in graph:
        print("  ".join(f"{val:3}" for val in row))