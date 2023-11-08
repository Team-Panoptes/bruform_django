# SOLUTION V1---------------------------------

def graph_matrix_to_list_v1(m):
    result = []
    for line in m:
        neighbours = []
        for i in range(len(line)):
            if line[i]:
                neighbours.append(i)
        result.append(neighbours)

    return result

# END SOLUTION V1-----------------------------

# SOLUTION V2---------------------------------

def graph_matrix_to_list_v2(m):
    result = []
    for line in m:
        neighbours = [i for i in range(len(line)) if line[i]]

        result.append(neighbours)

    return result

# END SOLUTION V2-----------------------------

# SOLUTION V3---------------------------------

def graph_matrix_to_list(m):
    # return [[i for i in range(len(m[j])) if m[j][i]] for j in range(len(m))]
    return [[i for i in range(len(line)) if line[i]] for line in m]
    
# END SOLUTION V3-----------------------------


m1 = [[False, True],
      [False, False]]

sol1 = [[1], []]

m2 = [[False, True, True],
      [True, False, False],
      [True, True, False]]

sol2 = [[1, 2], [0], [0, 1]]

print(graph_matrix_to_list(m1) == sol1)
print(graph_matrix_to_list(m2) == sol2)