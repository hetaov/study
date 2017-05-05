
def walk(G, s):

    Q, P = set(), dict()

    Q.add(s)

    P[s] = None

    while Q:

        u = Q.pop()

        for v in set(G[u]).difference(P):
            P[v] = u
            Q.add(v)

    return P

def components(G):

    L = list()

    seen = set()

    for u in G:

        if u in seen:
            continue

        C = walk(G, u)

        L.append(C)

        seen.update(C)

    return L

if __name__ == "__main__":

    G = {
            "a": {"b": 2, "d": 3},
            "b": {"c": 4, "e": 3},
            "c": {"e": 8, "f": 1},
            "d": {"b": 3},
            "e": {"a": 3},
            "f": {"a": 6}
        }

    #p = walk(G, "a")

    print components(G)
