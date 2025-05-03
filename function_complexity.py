import random
import math
import time
from functions_max_flow import ford_fulkerson, push_relabel  # Import des algorithmes

def generate_flow_problem(n):
    """
    Génère les matrices de capacité (C) et de coût (D) pour un problème de flot aléatoire.
    :param n: Nombre de sommets
    :return: Matrices C (capacités) et D (coûts)
    """
    # Initialisation des matrices C et D avec des zéros
    C = [[0] * n for _ in range(n)]
    D = [[0] * n for _ in range(n)]

    # Nombre d'arêtes non nulles à générer
    num_edges = math.floor((n ** 2) / 2)

    # Génération des arêtes avec des capacités et des coûts aléatoires
    edges = 0
    while edges < num_edges:
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        if i != j and C[i][j] == 0:  # Pas de boucle sur soi-même et pas de doublon
            C[i][j] = random.randint(1, 100)  # Capacité aléatoire entre 1 et 100
            D[i][j] = random.randint(1, 100)  # Coût aléatoire entre 1 et 100
            edges += 1

    return C, D

def print_matrices(C, D):
    """
    Affiche les matrices de capacité (C) et de coût (D).
    :param C: Matrice des capacités
    :param D: Matrice des coûts
    """
    print("Matrice des capacités (C) :")
    for row in C:
        print(" ".join(f"{val:3}" for val in row))
    
    print("\nMatrice des coûts (D) :")
    for row in D:
        print(" ".join(f"{val:3}" for val in row))

def measure_execution_times(C, D):
    """
    Mesure les temps d'exécution des trois algorithmes : Ford-Fulkerson, Push-Relabel, et Flot à coût min.
    :param C: Matrice des capacités
    :param D: Matrice des coûts
    """
    n = len(C)
    source = 0
    sink = n - 1

    # Mesure du temps pour Ford-Fulkerson
    start_ff = time.time()
    ford_fulkerson(C, source, sink)
    end_ff = time.time()
    theta_ff = end_ff - start_ff
    print(f"Temps d'exécution de Ford-Fulkerson (θFF(n)) : {theta_ff:.6f} secondes")

    # Mesure du temps pour Push-Relabel
    start_pr = time.time()
    push_relabel(C, source, sink)
    end_pr = time.time()
    theta_pr = end_pr - start_pr
    print(f"Temps d'exécution de Push-Relabel (θPR(n)) : {theta_pr:.6f} secondes")

# Exemple d'utilisation
if __name__ == "__main__":
    n = 10000  # Taille du graphe (nombre de sommets)
    C, D = generate_flow_problem(n)
    print_matrices(C, D)
    print("\nMesure des temps d'exécution :")
    measure_execution_times(C, D)