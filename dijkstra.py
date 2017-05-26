from heapq import heappush, heappop
from relax import relax

def dijkstrap(G, s):

    D, P, Q, S = {s: 0}, {}, [(0, s)], set()

    while Q:
        _, u = heappop(Q)

        if u in S: continue

        S.add(u)

        for v in G[u]:
            relax(G, u, v, D, P)
            heappush(Q, (D[v], v))

    return D, P

if __name__ == "__main__":
    
    W = {
            "a": {"b": 3, "c": 2},
            "b": {"d": 2},
            "c": {"b": -1, "e": 4},
            "d": {"c": 2},
            "e": {}
        }

    print dijkstrap(W, "a")
