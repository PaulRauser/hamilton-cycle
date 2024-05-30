import math
import pprint



word = input('Enter a word:') #1100111111

word_len = len(word)

# ((n-1) * n) / 2 = word_len - Umgeformt nach n (dimension)
dimensions = int(((1 + math.sqrt(1 + 8 * word_len)) / 2))

# RAW INPUT #1100111111
# Ziel [[1, 1, 0, 0], [1, 1, 1], [1, 1], [1]]


adjacency_matrix = []
all_circles_list = []



def hamilton_all(word):
    word_len = len(word)

    # ((n-1) * n) / 2 = word_len - Umgeformt nach n (dimension)
    dimensions = int(((1 + math.sqrt(1 + 8 * word_len)) / 2))

    all_circles = True
    start_hamilton_cycle(get_adjacency_matrix(word), all_circles)
    # print("Done, List: ", all_circles_list)
    return all_circles_list

def hamilton_one(word):
    word_len = len(word)

    # ((n-1) * n) / 2 = word_len - Umgeformt nach n (dimension)
    dimensions = int(((1 + math.sqrt(1 + 8 * word_len)) / 2))

    all_circles = False
    if start_hamilton_cycle(get_adjacency_matrix(word), all_circles) is None:
        return False
    else:
        return True


def get_adjacency_matrix(word):
    start = 0
    for i in reversed(range(dimensions - 1)):
        adjacency_matrix.append(list(word[start:start + i + 1]))
        start += i + 1

    #print("Adjacency Matrix: ", adjacency_matrix)
    return adjacency_matrix



# Tim mach weiter
start_knoten = 0







def get_neighbor_nodes(row: int, m):
    adjacency_row = []
    for col in range(len(m)):
        if col < row:
            v = m[col][row - col - 1]
            adjacency_row.append(v)
        else:
            v = m[row][col - row]
            adjacency_row.append(v)
    neighbors = []
    for i in range(len(adjacency_row)):
        if adjacency_row[i] == "1":
            if i >= row:
                neighbors.append(i+1)
            else:
                neighbors.append(i)
    #print("Neighbors: ", neighbors)
    return neighbors



def start_hamilton_cycle(m, all_circles):
    connected_nodes = []

    neighbors = get_neighbor_nodes(0, m) # Get Neighbours of startnode
    # [1,2]
    for neighbor in neighbors:
        connected_nodes.append([0, neighbor]) # create Array with path
        # [[0, 1], [0, 2]]

    return get_hamilton_cycle(connected_nodes, m, all_circles)




def get_hamilton_cycle(connected_nodes, m, all_circles):
    if connected_nodes:
        # print("Next run: Connected Nodes", connected_nodes)
        next_connected_nodes = []
        for node in connected_nodes:

            # [0,1] und [0,2]
            if len(node) == dimensions:
                if node[0] in get_neighbor_nodes(node[-1], m):
                    if all_circles:
                        # print("Node: ", node, "Next Connected Nodes: ", next_connected_nodes)
                        next_circle = node

                        next_circle.append(node[0])

                        all_circles_list.append(next_circle)
                        # print("Circle Appended")
                        # print("All Circles: ", all_circles_list)
                        # keine Ahnung ob benötigt: connected_nodes.pop(0)
                        # print("Node: ", node, "Next Connected Nodes: ", next_connected_nodes)
                    else:
                        # print("ONE CIRCLE FOUND", node)
                        next_circle = node
                        # print("Circle Appended", next_circle)
                        next_circle.append(node[0])
                        # print("Circle Appended", next_circle)
                        # print("Last Neighbor Node: ", get_neighbor_nodes(node[-1], m))
                        # print("Hamilton Cycle found:", node)
                        return next_circle



            else:
                neighbors = get_neighbor_nodes(node[-1], m)
                # print("Looking at", connected_nodes, " \n Node: ", node, " \n Neighbors:", neighbors)

                for neighbor in neighbors:
                    if neighbor not in node:

                        next_connected_nodes.append(node + [neighbor])

        return get_hamilton_cycle(next_connected_nodes, m, all_circles)


    #Rückgabe meherer Arrays, immer den letzen Wert nehmen und schauen ob ein Node noch nicht im Array ist
    #Bei Größe Array = anzahl der Knoten --> Hamilton Cycle

print(hamilton_all(word))







