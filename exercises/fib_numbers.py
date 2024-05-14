# generator solution
def fib_gen(final_index):
    n1 = 0
    n2 = 1
    for i in range(final_index):
        yield n1
        temp = n1
        n1 = n2
        n2 = temp + n2


for x in fib_gen(3):  # this for loop automatically iterates instead of using next(), just like range()
    print(x)

# list solution
def fib_list(final_index):
    my_list = [0,1]
    for i in range(2, final_index):
        my_list.append(my_list[i-2] + my_list[i-1])
    return my_list

print(fib_list(3))