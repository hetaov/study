# encode=utf-8

def relax(W, u, v, D, P):

    d = D.get(u, float('inf')) + W[u][v]

    print 'u is: %s, v is: %s' % (u, v)

    if d < D.get(v, float('inf')):
        D[v], P[v] = d, u

        return True

if __name__ == '__main__':
    W = {
            "a": {"b": 3, "c": 2},
            "b": {"d": 2},
            "c": {"b": 1}
        }
    D = {}
    P = {}
    D['a'] = 0
    print relax(W, 'a', 'c', D, P)

    print D
    print P
