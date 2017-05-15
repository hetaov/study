
def top_sort(G):

    count = {v: 0 for v in G}

    for u in G:

        for v in G[u]:
            count[v] += 1

    Q = [v for v in count if count[v] == 0]

    S = []

    while Q:

        u = Q.pop()

        S.append(u)

        for v in G[u]:
            count[v] -= 1
            if count[v] == 0:

                Q.append(v)

    return S


if __name__ == "__main__":
    G = {
            "a": {"b": 2},
            "b": {"c": 3},
            "f": {"a": 4},
            "c": {}
        }

    print top_sort(G)
