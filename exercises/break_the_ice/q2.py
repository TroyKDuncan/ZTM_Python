# Write a program which can compute the factorial of a given numbers.The results should be printed 
# in a comma-separated sequence on a single line.Suppose the following input is supplied to the 
# program: 8 Then, the output should be:40320

user_num = int(input('Enter a number: '))
result = 1
while user_num > 1:
    result *= user_num
    user_num -= 1

print(f'Result: {result}')