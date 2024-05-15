# built-in modules found at: https://docs.python.org/3/py-modindex.html

import random as r  # you can name the module or package something else, like numpy as np

print(r)
# help(r)
print(dir(r))

my_list = [1, 2, 3, 4, 5]

print(r.random())  # returns a float number between 0 an  1
print(r.randint(1, 10))  # returns an int from param1 to param2
print(r.choice(my_list))  # picks something from the iterable
print(r.shuffle(my_list))  # happens in place, so returns none
print(my_list)
print()

import sys

print(sys)

print(sys.argv[0])  # argv starts with the file name, so this will print the file name
first_name = sys.argv[1]
last_name = sys.argv[2]
print(f'Hi there, {first_name} {last_name}')               