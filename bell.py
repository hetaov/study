# encode=utf-8

from relax import relax

def bell(G, s):
    
    D = {s: 0 }
    P = {}

    for rnd in G:

        changed = False

        for u in G:
            for v in G[u]:
                if relax(G, u, v, D, P):
                    changed = True

        if not changed:
            break

    else:
        print 'nagitive '

    return D

if __name__ == "__main__":
    
    W = {
            "a": {"b": 3, "c": 2},
            "b": {"d": 2},
            "c": {"b": 1, "e": 4},
            "e": {"b": 2},
            "d": {"c": 3}
        }

    print bell(W, "a")
