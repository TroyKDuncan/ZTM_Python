# Write a program that calculates and prints the value according to the given formula:

# Q = Square root of [(2 _ C _ D)/H]

# Following are the fixed values of C and H:

# C is 50. H is 30.

# D is the variable whose values should be input to your program in a comma-separated sequence.
# For example Let us assume the following comma separated input sequence is given to the program:

# 100,150,180

# The output of the program should be:

# 18,22,24

from math import sqrt


sequence = '100,150,180'
c = 50
h = 30

# splits the sequence by commas and converts everything into ints and adds them to a list
split_sequence = list(map(lambda x: int(x), sequence.split(',')))

# performs the calculation sqrt((2*c*d)/h) on each value un split sequence and rounds before appending to result
result = list(map(lambda d: round(sqrt((2*c*d)/h)), split_sequence))
print(result)
