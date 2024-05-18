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