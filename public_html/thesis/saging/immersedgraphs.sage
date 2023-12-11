
subsize3s=[[1,2,3],[0,2,3],[0,1,3],[0,1,2]]

oct3curveseq = [ [0,1,2], [1,2,3] ]

def isect(a,b):
    c = [foo for foo in a if foo in b]
    return c

possibocts = [oct3curveseq]

for foo in range(2):
    possibocts = [ foo + [bar] for foo in possibocts for bar in subsize3s]

decentocts = []

for oct in possibocts:
    goodisects=True
    tszujoct=[]
    for foo in range(-1,3):
        a=oct[foo]
        b=oct[foo+1]
        octisect = isect(a,b)
        goodisects = (goodisects and (len(octisect)==2))
        aa = [bar for bar in b if bar not in a] + octisect
        tszujoct.append(set(aa))
        # tszujoct = b
    if goodisects:
        decentocts.append(tszujoct)

def relabeloct( oct, a, b):
    def swapper(x):
        if x == a: return b
        elif x == b: return a
        else: return x
    noct = []
    for s in oct:
        t = [swapper(foo) for foo in s]
        noct.append(set(t))
    return noct

goodocts=[]
for oct in decentocts:
    noct = relabeloct( oct, 1, 2)
    if (noct not in goodocts) and (oct not in goodocts):
        goodocts.append(oct)
