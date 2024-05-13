# print out items that have duplicates
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# Using comprehensions

# my solution
duplicates = list({a for a in some_list if some_list.count(a) > 1})
print(duplicates)
