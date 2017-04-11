
def link(C, u):

    while C[u] and C[u] != u:
        u = C[u]
    return u

def union(C, u, v):

    u = link(C, u)
    v = link(C, v)

    C[u] = v

if __name__ == "__main__":

    G = {
            "a": {"b": 2, "d": 3},
            "b": {"c": 4, "e": 3},
            "c": {"e": 8, "f": 1},
            "d": {"b": 3},
            "e": {"a": 3},
            "f": {"a": 6}
        }

    #C = [{u: v} for u in G for v in G[u]]
    
    C = {u: u for u in G}

    E = [(G[u][v], u, v) for u in G for v in G[u]]

    print C
    for _, u, v in sorted(E):

        if link(C, u) != link(C, v):
            union(C, u, v)

    print C
