
def print_test(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Ceci est un, {name}')  # Press ⌘F8 to toggle the breakpoint.


def graph_import(link):
    with open(link, 'r') as f:
        lines = f.readlines()

    graph = []  # Liste pour stocker le graphe
    parents = set()  # Stocke les nœuds qui sont des parents (prédécesseurs)
    predecessors = set()  # Stocke tous les nœuds existants

    # Lire et structurer les données du fichier
    for line in lines:
        values = list(map(int, line.split()))  # fais un vecteur avec les valeurs de la ligne (1 1 => [1,1])

        if values[1] < 0 : # Test si la valeur de liens ne sont pas négatifs
            return -1 # Doit etre pris en charge dans le main avec une comparaison

        predecessors.update(values[2:])  # Noeuds parents

        graph.append(values)  # Stocker la ligne
        # Ajouter les prédécesseurs à l'ensemble des parents

    # implémenter la fonction de test circuit
    if test_no_circuit_in_graph(graph) == -1 :
        return -2

    for line in graph:
        if len(line) < 3:
            line.append(0)

    # Déterminer les nœuds sans successeur (ceux qui ne sont jamais parents)
    omega = [len(graph) + 1, 0]  # initialisation d'oméga [dernier_noeud + 1, 0]
    for i in range(len(graph)):
        if i+1 not in predecessors:  # S'il n'est jamais parent, il va vers omega
            omega.append(i+1)

    # Déterminer les nœuds sans prédécesseur (ceux qui ne sont jamais enfants)
    alpha = [0, 0]  # α est toujours [0, 0]

    # Insérer alpha au début du graphe
    graph.insert(0, alpha)
    # Ajouter omega à la fin du graphe
    graph.append(omega)

    print("Graphe final :")
    for line in graph:
        print(line)

    return graph



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_test('test')


