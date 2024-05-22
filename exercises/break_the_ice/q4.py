# Write a program which accepts a sequence of comma-separated numbers from console and generate 
# a list and a tuple which contains every number.Suppose the following input is supplied to the program:

# 34,67,55,33,12,98

# Then the output should be:

# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

sequence = '34,67,55,33,12,98'
split_sequence = sequence.split(',')
my_list = []
for c in split_sequence:
    my_list.append(int(c))
my_tuple = tuple(my_list)

print(my_list)
print(my_tuple)