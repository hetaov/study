from mem import mem

def get_L(seq):

    @mem
    def L(cur):

        res = 1
        for pre in range(cur):
            if seq[pre] <= seq[cur]:
                res = max([res, 1 + L(pre)])

        return res

    return max([L(i) for i in range(len(seq))])

if __name__ == "__main__":
    seq = [2, 3, 1, 5, 3, 1, 8, 9]
    print get_L(seq)
