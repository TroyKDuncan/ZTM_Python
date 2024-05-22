# With a given integral number n, write a program to generate a dictionary that contains (i, i x i) 
# such that is an integral number between 1 and n (both included). and then the program should 
# print the dictionary.Suppose the following input is supplied to the program: 8

# Then, the output should be:

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

user_num = int(input('Enter a number: '))
result = {}
for num in range(1, user_num + 1):
    result[num] = num ** 2
print(result)