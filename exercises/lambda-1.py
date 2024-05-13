# Challenge 1: sqaure the list and print with lambda expressions
my_list = [5, 4, 3]

print(list(map(lambda item: item ** 2, my_list)))

# Challenge 2: sort a list of tuples based on the second value
a = [(0, 2), (4, 3), (9, 9), (10, -1)]

a.sort(key=lambda pair: pair[1])  # sort by the second item, VERY COMMON
print(a)
