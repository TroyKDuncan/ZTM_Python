# functions are basically treated as variables in python

def hello():
    print('helloooooo')


greet = hello
print(greet())
del hello
print(greet())  # even though hello function was deleted, python knows that greet is still pointing to it and doesn't delete it completely

# Higher order functions


def greet(func):  # a function that accepts a function as a parameter
    func()


def greet2():
    def func():
        return 5
    return func


print(greet2())


# Decorators super charge functions
print()

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('**********')
        print()
        func(*args, **kwargs)
        print()
        print('**********')
    return wrap_func

# @my_decorator
# def hello():
#     print('helloooooo')

# @my_decorator
# def bye():
#     print('adios muchacho')

# hello()
# bye()
# print()

@my_decorator
def hello2(greeting, emoji=':('):
    print(greeting, emoji)

hello2('hey gurrrl')

### DECORATOR PATTERN ###

# def my_decorator(func):
#     def wrap_func(*args, **kwargs):
#         func(*args, **kwargs)
#     return wrap_func
print()
