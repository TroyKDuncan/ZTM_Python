print(__name__)

def buy(*args, **kwargs):
    cart = []
    for item in args:
        cart.append(item)
    return cart

if __name__ == '__main__':  # __name__ is the name of a given file, and __main__ is the __name__
    print ('This is main')  # of whatever file you are running