from functools import wraps

def mem(func):

    cache = {}

    @wraps(func)
    def wrap(*args):

        if args not in cache:
            cache[args] = func(*args)

        return cache[args]

    return wrap

@mem
def test(num):
    return num * 2

if __name__ == "__main__":
    
    #test = mem(test)

    print test(2)
    print test(3), test(2)
    print test(3)
