# Betty war hier
import math

def create_matrix(input_word):
    nodes = int(((1 + math.sqrt(1 + 8 * len(input_word))) / 2))
    matrix = [[0] * nodes for _ in range(nodes)]
    index = 0
    for i in range(nodes):
        for j in range(i + 1, nodes):
            matrix[i][j] = int(input_word[index])
            matrix[j][i] = matrix[i][j]
            index += 1
    return matrix 

#print(create_matrix("1100111111"))

def find_hamilton_cycles(input_word, find_all=False):
    graph = create_matrix(input_word)
    nodes = int(((1 + math.sqrt(1 + 8 * len(input_word))) / 2))
    path = [-1] * nodes
    path[0] = 0
    results = []

    def search(graph, path, position):
        if position == nodes:
            if graph[path[position - 1]][path[0]] == 1:
                completed_path = path.copy() + [path[0]]
                results.append(completed_path)
                return not find_all 
            return False
        for v in range(1, nodes):
            if graph[path[position - 1]][v] == 1 and v not in path:
                path[position] = v
                if search(graph, path, position + 1):
                    return True
                path[position] = -1
        return False

    search(graph, path, 1)
    return results

def hamilton_one(input_word):
    results = find_hamilton_cycles(input_word)
    return bool(results)

def hamilton_all(input_word):
    return find_hamilton_cycles(input_word, find_all=True)

input_word = "1100111111"
first_cycle = hamilton_one(input_word)
if first_cycle:
    print("Hamiltonkreis:", first_cycle)
else:
    print("Kein Hamiltonkreis gefunden.")

all_cycles = hamilton_all(input_word)
if all_cycles:
    for cycle in all_cycles:
        print("Hamiltonkreis:", cycle)
    print(f"Anzahl der Hamiltonkreise: {len(all_cycles)}")
else:
    print("Keine Hamiltonkreise gefunden.")

