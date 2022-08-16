import numpy as np
# n vertices and len(sequence)=n-2

# Given sequence and number of vertices
given_set = [1, 2, 3, 4]
num_vertices = len(given_set) + 2

# Create list that is all numbers 1 to n
range_set = []
count = 1
while len(range_set) < len(given_set)+2:
    range_set.append(count)
    count += 1
# print(range_set)
print("These are the edges of the tree: ")
# get difference between range and set
i = 0
v = len(given_set)-2
while i in range(0, len(given_set)):
    x_value = given_set[0]                              # first entry of sequence
    y_value = min(set(range_set) - set(given_set))      # minimum value in range not in sequence
    given_set.append(y_value)
    given_set.pop(0)
    i += 1
    print((x_value, y_value))
else:
    edge = list(set(range_set) - set(given_set))
    print((edge[0], edge[1]))





