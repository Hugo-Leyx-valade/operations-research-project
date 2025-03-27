from functions import *

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    imported_data = graph_import("graphs/graph1.txt")
    graph = imported_data[0]
    flow_type = imported_data[1]
    if flow_type == 1:
        print("problème de flow à cout minimal")
    else:
        print("problème de cout maximal") #méthode F-F ou pousser-réétiqueter

    print_graph_to_matrix_of_values(graph)

    if flow_type == 2:  # flot max
        print_graph_to_matrix_of_values(graph)
        ff_mat = ford_fulkerson(graph)[1]

    compute_flow_matrix(graph,ff_mat)