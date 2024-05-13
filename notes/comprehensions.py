# list, set, dictionary comprehensions

# LIST 

my_list = []
for char in 'hello':
    my_list.append(char)

print(my_list)

# OR you can do this:

# basically choose a variable and then run a for loop to add things to the list

my_list = [char for char in 'hello']
print(my_list)

# create a list with numbers ranging from 0 - 99
my_list2 = [i for i in range(0, 100)]
print(my_list2)

# create a list that has numbers from 0 - 99 multiplied by 2
my_list3 = [num*2 for num in range(0, 100)]
print(my_list3)

# only keep even numbers from list 3
my_list4 = [num**2 for num in range(0, 100) if num % 2 == 0]
print(my_list4)


# SET: same stuff as lists, but only contains unique items
print()

# DICTIONARIES

simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {k:v**2 for k, v in simple_dict.items()}
my_dict2 = {k:v**2 for k, v in simple_dict.items() if v%2==0}

print(my_dict)
print(my_dict2)

my_dict3 = {num:num*2 for num in [1,2,3]}
print(my_dict3)
