from collections import Counter, defaultdict, OrderedDict

li = [1,2,3,4,5,6,7,13,3,2,4,6,4,3,1,2,1,2]
print(Counter(li))

dictionary = {'a': 1, 'b':2}
print(dictionary['a'])
dictionary = defaultdict(lambda: 'not found', {'a': 1, 'b':2})  # common pattern 
print(dictionary['a'])
print(dictionary['c'])  # if it's not already in the dict, it sends the DEFAULT

d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d == d2)  # false because order matters, unlike normal dictionaries


import datetime as dt

print(dt.time(5,45,32,654))  # create time objects
print(dt.date.today())  # prints out today's date


import time

# used this one for measuring the performance of our functions with decorators


from array import array

arr = array('i', [1,2,3])

print(arr[0])