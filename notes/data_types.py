# Fundamental data types

##### int and float

# print(2 + 6) #int
# print(2 - 6) #int
# print(2 * 6) #int
# print(2 / 6) #float

# print(20 + 1.7) #float
# print(int(20 + 1.7)) #int typecasting removes anything after the decimal without roundng
# print(2 ** 3) #int 2 to the power of 3
# print(2 // 4) #int representing a whole number of times the second value can go into the first
# print(5 // 4) #int representing a whole number of times the second value can go into the first
# print(5 % 4) #int representing a whole number remainder after division, also works with floats

# inherent math functions -> find them all using Google

# print(round(3.1)) #rounds
# print(round(3.5)) #rounds
# print(abs(-20)) #absolute value
# print(bin(abs(-20))) #changes to binary representation

# floats take up more space than ints

##### strings are immutable, the only way to  change it is to reassign

# print(type("hi"))
# username = 'me'
# password = 'password'
# long_string = '''
# WWWWW
#  O O
#  ---
# '''
# print(long_string) #multiline strings
# first_name = 'Troy'
# last_name = 'Duncan'
# full_name = first_name + ' ' + last_name
# print(full_name)
# # \t means tab, \n means newline
# print(f'Hello {full_name}, how are you?')

# selfish = 'me me me'
# print(selfish[0])
# # selfish[start:stop:stepover]
# print(selfish[0:7:2]) #prints everything starting at 0 and doesn't print the stop value
# print(selfish[::-1]) #prints backwards

# print(len('Hey there, buddy'))

# quote = '    To be, or not to be    '
# print(quote.upper())
# print(quote.capitalize())
# print(quote.lower())
# print(quote.find('or')) # returns index of the start of the first instance
# print(quote.strip())
# print(quote.replace('be', 'BUTT'))
# print(quote.replace(' ', ''))
# print(quote)
# quote = quote.strip()
# print(quote)

##### bools are True or False, nonzero or 0 respectively

# name = 'Troy'
# is_cool = False
# is_cool = True
# print(is_cool)

# print(bool(90))
# print(bool(0))

### list, our first Data Structure

# li = [1,2,3,4,5]
# li2 = ['a','b','c']
# li3 = [1,2,'a', True] # can contain any number of any object, not contrained to one type

# amazon_cart = ['notebooks', 'sunglasses']
# print(amazon_cart[0])
# print(amazon_cart[1])

# amazon_cart = [
#   'notebooks',
#   'batteries',
#   'toys',
#   'grapes'
# ]
# print(amazon_cart[0:3:2]) # sclicing
# amazon_cart[0] = 'pizzas' # mutable
# print(amazon_cart)

# new_cart = amazon_cart # this links them; it doesn't copy the values to the new variable
# new_cart[0] = 'WOW'
# print(amazon_cart)
# new_cart = amazon_cart[:] # using slicing allows you to copy the values without linking
# new_cart[0] = 'mmmm'
# print(f'{amazon_cart} {new_cart}')

# matrix = [ # 2D arrays
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]
# print(matrix[0][2])
# print(matrix[1][1])
# print(matrix[2][0])
# matrix = [ # how computers see images; this can represent an X
#   [1,0,1],
#   [0,1,0],
#   [1,0,1]
# ]

# adding methods
# basket = [1,2,3,4,5]
# print(len(basket))
# new_list = basket.append(3) # append is done "in place", meaning in this case it isn't a value
# print(new_list)
# print(basket)
# new_list = basket.copy() # returns a copy of the list without slicing
# new_list.append(8)
# print(new_list)
# basket.insert(3, 100) # places the second value in the first value's index and
#                       # pushes everything back; also done in place
# print(basket)
# basket.extend(new_list) # concatenates the list with another iterable
# print(basket)
# basket.extend('Hello') # each index of the iterable is given its own index
# print(basket)

# # removing methods
# basket.pop() # removes the end by default, or the given index in the argument; returns the value
# print(basket)
# basket.remove(3) # removes the first instance of the argument
# print(basket)
# basket.clear() # empties the list
# print(basket)

# basket.extend(['c','a','b','d','e'])

# print(basket.index('c')) # return the index of the value
# # print(basket.index('c', 0, 2)) # checks for 'c' starting at 0 and stopping before 2
# print(basket.index('c', 0, 3))
# print('d' in basket) # returns value of boolean expression

# print(basket.count('a')) # returns an int
# print(type(basket.count('a')))

# print(sorted(basket)) # returns a new list without modifying basket
# print(basket)
# basket.sort() # modifies in place
# print(basket)
# print(basket.reverse()) # modifies in place
# print(basket)

# # common list patterns

# basket.sort()
# basket.reverse()
# print(basket[::-1]) # very commonly used
# print(basket)
# new_list = list(range(100)) # starts from 0 and ends before 100
# print(new_list)
# new_list = list(range(1,100)) # starts from 1 and ends before 100
# print(new_list)

# spacer = '!'
# sentence = spacer.join(['hi','my','name','is','Troy'])
# print(sentence)
# spacer = ' '
# sentence = spacer.join(['hi','my','name','is','Troy'])
# print(sentence)
# sentence = ' '.join(['hi','my','name','is','Troy']) # commonly used
# print(sentence)

# list unpacking

# a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
# print(a)
# print(b)
# print(c)
# print(other)
# print(d)

# None, the absence of value

# weapons = None
# print(weapons)

# dictionary, another Data Structure

# dictionary = { # key:value pairs, not indexes
#   'a': [1,2,3], # dictionaries can hold lists and lists can hold dictionaries
#   'b': 'Hello',
#   'x': True
# }
# print(dictionary['a']) # returns the value associated with the key
# print(dictionary['a'][1]) # returns the value associated with the key

# dictionary = {
#   'a': [1,2,3],     # keys must be immutable data types, which excludes dictionaries and lists
#   2: 'Hello',       # 95% of the time, keys are descriptive strings or numbers
#   '[1,2,3]': True   # keys must be unique, else they overwrite each other 
# }
# print(dictionary['[1,2,3]']) # returns True

# Dictionary methods

# user = {
#   'basket': [1,2,3],
#   'greet': 'hello',
#   'age': 20
# }
# print(user.get('age', 55)) # tries to get a value pointed to by the key without causing an error
#                            # if it is there, it uses the value already there, else it uses the
#                            # second argument as a default value

# user2 = dict(name='JohnJohn') # not very common way of making a dictionary
# print(user2)

# print('basket' in user) # checks keys by defaul
# print('hello' in user)
# print('hello' in user.keys())
# print('hello' in user.values())
# print(user.items())
# print(user.pop('basket')) # return the argument key's value and removes it from the dictionary
# print(user)
# print(user.update({'age': 55}))
# print(user)
# print(user.clear())       # in place removes everything, just like with lists
# user = user2.copy()       # works just like lists
# print(user)

# tuples are immutable, but still indexable and are usually faster

# my_tuple = (1,2,3,4,5) # only has count() and index() as methods
# print(5 in my_tuple)

# sets are unordered collections of unique objects

# my_set = {1,2,3,4,5,5,6,6,7}
# my_set.add(100)
# my_set.add(3)
# print(my_set)

# my_list = [1,2,3,4,5,5,6,6,7]
# my_set = set(my_list)
# my_set.add(100)
# my_set.add(3)
# print(my_set)

# print(1 in my_set)
# print(my_set[3])

# set methods

# my_set = {1,2,3,4,5,}
# your_set = {4,5,6,7,8,9,10}

# print(my_set.difference(your_set))
# my_set.discard(5)print
# .difference_update()
# .intersection()
# .isdisjoint()
# .issubset()
# .issuperset()
# .union()

# complex

# Classes -> custom types

# Specialized Data Types -> found in modules