g=Graph(6,multiedges=True)
g.allow_multiple_edges(True)
graphlist = [g]
maybeedge = [(0,1), (0,2), (0,3), (0,4), (1,2), (1,3), (1,4), (2,3), (2,4), (3,4)]
yesedges = [[e] for e in maybeedge]

def nographinlist( g, ll ):
    if not ll:
        return True
    else:
        foo = g.is_isomorphic(ll[0])
        for h in ll: foo = foo or g.is_isomorphic(h, edge_labels=True)
        return not foo


edgelists = copy(yesedges)
for ednum in range(3 -1):
    edgelists = [ foo + bar for foo in edgelists for bar in yesedges]

glist = [ Graph( [[0,1,2,3,4],foo], multiedges=True)  for foo in edgelists]

keepers =[]
for g in glist:
    if nographinlist( g, keepers):
        keepers.append(g)
print(len(keepers))
