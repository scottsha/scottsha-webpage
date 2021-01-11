import itertools as it

anuli=[foo for foo in it.permutations(range(6)) if foo[1]<foo[2] and foo[3]<foo[4] and foo[4]<foo[5] ]

sample_size = len(anuli)

def is_edge( i, j):
    inn = anuli[i]
    inns = set([inn[0],inn[1],inn[2]])
    out = anuli[j]
    outs = set([out[3],out[4],out[5]])
    if inns == outs:
        return True
    else:
        return False

the_edges = [ (i,j) for i in range(sample_size) for j in range(sample_size) if (i<j and is_edge(i,j))]

G=Graph(the_edges)