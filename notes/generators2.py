from my_decorators import performance


# @performance
# def long_function():
#     print('1')
#     for i in range(100000000):
#         i*5


# @performance
# def long_function2():
#     print('2')
#     for i in list(range(100000000)):
#         i*5

# long_function()  # using a generator, less memory
# long_function2()  # creating a list, more memory and took over twice as long
# print()


def gen_fun(num):  # how to create a genereator
    for i in range(num):
        yield i

g = gen_fun(5)
print(next(g))
print(next(g))
print(next(g))
print(next(g))

for i in gen_fun(5):
    print(i)

# # how for loops work
# def special_for(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(iterator)
#             print(next(iterator) * 2)
#         except StopIteration:
#             break

# special_for([1,2,3])

# # range() mimic
# class MyRange:
#     current = 0
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if MyRange.current < self.last:
#             num = MyRange.current
#             MyRange.current += 1
#             return num
#         raise StopIteration
    
# gen = MyRange(0,100)
# for i in gen:
#     print(i)
