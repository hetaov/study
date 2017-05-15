from mem import mem

def find_min_path(W, s, t):

    @mem
    def d(u):
        if u == t: return 0
        print W[u]
        return min([W[u][v] + d(v) for v in W[u]])

    return d(s)

if __name__ == "__main__":

    G = {
            "a": {"b": 2, "c": 3},
            "b": {"c": 1, "e": 2},
            "c": {"d": 1, "f": 1},
            "d": {"e": 3},
            "e": {"f": 1},
            "f": {}
    }

    print find_min_path(G, "a", "f")
