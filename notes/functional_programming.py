# Functional Programming - separating functions and data instead of combining

'''
1. Pure Functions
    - Rule 1: The same input always results in the same output
    - Rule 2: The function doesn't affect the outside world
        - if a function is supposed to do a calculation, it doesn't print something too
'''

# This example is good because it doesn't interact with the outside world.
# It doesn't change what is passed, it doesn't print anything, etc.


from functools import reduce


def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


print(multiply_by2([1, 2, 3, 4]))


# This is bad because it is changing something outside of the function, even though
# it is producing the same output.


new_list = []


def multiply_by2(li):
    for item in li:
        new_list.append(item * 2)
    return new_list


print(multiply_by2([1, 2, 3, 4]))


# This is bad because it is calling the print function and interacting with the
# outside world.


def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    print(new_list)


multiply_by2([1, 2, 3, 4])

# Map function
# map() takes two inputs, a function and an iterable and performs the function on
# everything in the iterable
print()

my_list = [1, 2, 3, 4]


def multiply_by2(item):  # notice it isn't taking a list; it's performing this
    return item * 2      # on everything inside the iterable linked to it with map()


print(map(multiply_by2, my_list))  # this returns a map object
print(list(map(multiply_by2, my_list)))  # this typecasts it into a list
print(my_list)  # notice my_list isn't affected, so it stays pure

# Filter Function
print()


def only_odd(item):
    return item % 2 != 0  # Uses a boolean expression to perform checks and removes
    # items from the iterable that return a false value.
    # It still doesn't change the original.


print(filter(only_odd, my_list))  # like map, takes a function and iterable
print(list(filter(only_odd, my_list)))  # must be typecast
print(list(filter(only_odd, map(multiply_by2, my_list))))
print(my_list)

# Zip Function - returns tuples of indeces
# for example: list(zip([1,2,3], [10,20,30])) -> [(1,10),(2,20),(3,30)]
# dicts: use .keys(), .values(), or .items() to specify what to return
# .items() returns tuples of key: value pairs
print()

my_list = [1, 2, 3, 4]
your_dict = {
    'me': 1,
    'you': 2,
    'them': 3
}
their_tuple = (5, 10, 15)

print(zip(my_list, your_dict, their_tuple))  # return a zip object
print(list(zip(my_list, your_dict, their_tuple)))
print(list(zip(my_list, your_dict.keys(), their_tuple)))
print(list(zip(my_list, your_dict.values(), their_tuple)))
print(list(zip(my_list, your_dict.items(), their_tuple)))


# Reduce Function
print()


# this one is complicated, but here are some examples:

# summing contents of a list:

def add(a, b):
    return a + b


numbers = [1, 2, 3, 4, 5]
total = reduce(add, numbers)
print(total)

# finding max or min:


def max(a, b):
    if a > b:
        return a
    else:
        return b


numbers = [1, 2, 3, 4, 5]
maximum = reduce(max, numbers)
print(maximum)

# checking if all values are true:


def all_true(a, b):
    return a and b


values = [True, True, True, True, True]
all_true = reduce(all_true, values)
print(all_true)

# checking if any values are true


def any_true(a, b):
    return a or b


values = [False, False, False, False, True]
any_true = reduce(any_true, values)
print(any_true)
