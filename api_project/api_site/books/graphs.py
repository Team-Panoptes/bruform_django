ex1 = [(0, 1)]

ex2 = [(4, 5), (7, 8), (0, 2), (1, 3), (2, 6), (0, 1), (1, 4)]



def is_ancestor(l, a, b):
    def find_ancestors(l, elem):
        return [arc[0] for arc in l if arc[1] == elem]
    
    ancestors = find_ancestors(l, a)
    while ancestors:
        if b in ancestors:
            return True

        ancestors += find_ancestors(l, ancestors.pop())
    return False

print(is_ancestor(ex2, 5, 1))