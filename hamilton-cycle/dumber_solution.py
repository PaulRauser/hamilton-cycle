# Beispiel Haus vom Nikolaus
import math
import pprint

word = '1100111111'  #input('Enter a word:') #1100111111

word_len = len(word)

# ((n-1) * n) / 2 = word_len - Umgeformt nach n (dimension)
dimensions = int(((1 + math.sqrt(1 + 8 * word_len)) / 2))

# RAW INPUT #1100111111
# Ziel [[1, 1, 0, 0], [1, 1, 1], [1, 1], [1]]

word_array = []
start = 0

for i in reversed(range(dimensions - 1)):
    word_array.append(list(word[start:start + i + 1]))
    start += i + 1

pprint.pprint(word_array)

# TIm mach weiter
start_node = 0


connected_nodes = []









