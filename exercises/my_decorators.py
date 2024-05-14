from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'Time elapsed for {fn}: {round(t2 - t1, 2)} ms')
        return result
    return wrapper