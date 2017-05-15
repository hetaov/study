from top_sort import top_sort

def min_path(G, s, t):

    Q = {v: float("inf") for v in G}

    Q[s] = 0
    
    for u in top_sort(G):
        if u == t: break
        for v in G[u]:
            Q[v] = min(G[u][v] + Q[u], Q[v])

    return Q[t]


if __name__ == "__main__":

    G = {
            "a": {"b": 2, "c": 3},
            "b": {"c": 1, "e": 2, "f": 1},
            "c": {"d": 1, "f": 1},
            "d": {"e": 3},
            "e": {"f": 1},
            "f": {}
    }

    print min_path(G, "a", "f")
