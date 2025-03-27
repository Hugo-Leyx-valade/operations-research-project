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