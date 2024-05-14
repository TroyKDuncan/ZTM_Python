'''
### Exercise 1 ###
Write a program which will find all such numbers which are divisible by 7 but are not a multiple 
of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a 
comma-separated sequence on a single line.
'''
# nums = []
# for num in range(2000, 3201):
#     if num % 7 == 0 and num % 5 != 0:
#         nums.append(str(num))

# print(','.join(nums))

'''
### Exercise 2 ###
Write a program which can compute the factorial of a given numbers.The results should be printed 
in a comma-separated sequence on a single line.Suppose the following input is supplied to the 
program: 8 Then, the output should be:40320
'''
# while True:
#     try:
#         user_num = int(input('Enter an integer: '))
#     except ValueError:
#         print('Invalid input')
#     else:
#         break

# def factorial(num):
#     if num == 0:
#         return 1
#     return num * factorial(num - 1)

# print(factorial(user_num))

'''
### Exercise 3 ###
With a given integral number n, write a program to generate a dictionary that contains (i, i x i) 
such that is an integral number between 1 and n (both included). and then the program should print 
the dictionary.Suppose the following input is supplied to the program: 8

Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
'''
# while True:
#     try:
#         user_num = int(input('Enter an integer: '))
#     except ValueError as err:
#         print(err)
#     else:
#         break

# result = {}
# for num in range(1, user_num + 1):
#     result[num] = num ** 2

# print(result)

