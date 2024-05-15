# Generators

def make_list(n):
    result = []
    for i in range(n):
        result.append(i*2)
    return result


# lists are held in memory, but range gives things one by one
my_list = make_list(100)
print(my_list)


# general way to create a generator
def generator_function(num):
    for i in range(num):
        yield i * 2


g = generator_function(100)

next(g)
next(g)
next(g)
next(g)

def do_something():
    print('Blah blah blah')


do_something()
do_something()
do_something()
do_something()

print(next(g))  # the yield keeps track of where it is at in the range