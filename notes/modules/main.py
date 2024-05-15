# import utility  # kinda messy
# import shopping.shopping_cart  # kinda messy
# instead do this:
# from utility import *  # this imports all the functions from the module, being specific is better
from utility import multiply, divide  # import actual functions that can be used by name
from shopping.shopping_cart import buy  
# if you might have name collisions, you might want to import and reference the module name
# for example: two different modules use functions with the same name, so you want to specify
# where they are coming from

if __name__ == '__main__':  # __name__ is the name of a given file, and __main__ is the __name__
    print ('This is main')  # of whatever file you are running
    print(multiply(2, 3))
    print(divide(2, 3))
    print(buy)
    print(buy('item', 'apple', 'banana', 'kiwi'))
    