import math

# ----------------------------------------
# Word array generation
word = '1100111111'  #input('Enter a word:') #1100111111 #Michis Wort: 0101011100
# -----------------------------------

# build edges from word
def findEdges(word):
    word_len = len(word)

    dimensions = int(((1 + math.sqrt(1 + 8 * word_len)) / 2))

    word_array = []
    start = 0

    for i in reversed(range(dimensions - 1)):
        word_array.append(list(word[start:start + i + 1]))
        start += i + 1

    edges = []
    for i in range(dimensions - 1):
        for j in range(len(word_array[i])):
            if word_array[i][j] == '1':
                edges.append(tuple((i, i + j + 1)))
                edges.append(tuple((i + j + 1, i)))
    return edges, dimensions

# -------------------------------------
# Find one cycle
# hamilton_one: (word) return one list 
def hamilton_one(word):
    edges, dimensions = findEdges(word)
    start_node = 0
    current_path = [start_node]
    paths = []
    current_node = current_path[-1]

    while(len(current_path) != 0):
        #Set current node
        current_node = current_path[-1]
        # If current cycle not visited yet, add it
        if not current_path.copy() in paths:
            paths.append(current_path.copy())

        node_found = None
        # Check every edge
        for edge in edges:
            # If first node of edge is current edge and current path contains all nodes and next node is start node
            if edge[0] == current_node and len(current_path) == dimensions and edge[1] == start_node:
                # Cycle found
                hamilton_cycle = current_path.copy()
                hamilton_cycle.append(edge[1])
                return True

            # If first node is current node and next node not in current path
            elif(edge[0] == current_node and (not edge[1] in current_path)):
                new_cycle = current_path.copy()
                new_cycle.append(edge[1])

                # Check if potential next path is in paths
                if(new_cycle not in paths):
                    node_found = edge[1]

        # What to do if a node was found 
        if node_found != None:
            current_path.append(node_found)
        
        # What to do if no node was found
        else:
            current_path.pop()
    
    return False

# -----------------------------------------------------
#Find all cycles
def hamilton_all(word):
    edges, dimensions = findEdges(word)
    start_node = 0
    current_path = [start_node]
    paths = []
    current_node = current_path[-1]

    hamilton_cycles = []
    while(len(current_path) != 0):
        # Set current node
        current_node = current_path[-1]
        # If current cycle not visited yet, add it
        if not current_path.copy() in paths:
            paths.append(current_path.copy())

        node_found = None
        # Check every edge
        for edge in edges:
            # If first node of edge is current edge and current path contains all nodes and next node is start node
            if edge[0] == current_node and len(current_path) == dimensions and edge[1] == start_node:
                # Cycle found
                hamilton_cycle = current_path.copy()
                hamilton_cycle.append(edge[1])
                hamilton_cycles.append(hamilton_cycle)
            
            # If first node is current node and next node not in current path
            elif(edge[0] == current_node and (not edge[1] in current_path)):
                new_cycle = current_path.copy()
                new_cycle.append(edge[1])

                # Check if potential next path is in paths
                if(new_cycle not in paths):
                    node_found = edge[1]

        # What to do if a node was found 
        if node_found != None:
            current_path.append(node_found)
            current_path[-1]
        
        # What to do if no node was found
        else:
            current_path.pop()

    return hamilton_cycles

# ----------------------------------------------
# Testing
print(hamilton_one(word))
print(hamilton_all(word))