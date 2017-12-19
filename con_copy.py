from mem import mem

def con(a, b):

    @mem
    def L(i, j):
        if min(i, j) < 0: return 0
        if a[i] == b[j]: return 1 + L(i - 1, j - 1)
        else: return max(L(i-1, j), L(i, j - 1))

    return L(len(a) - 1, len(b) - 1)

if __name__ == "__main__":

    a = ['s', 't', 'u', 'c', 'k', 'b', 'u', 'k', 'e', 'r']
    b = ['s', 't', 'u', 'c', 'k', 'k', 'e', 'r', 't']

    print con(a, b)
