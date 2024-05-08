### conditional logic ###

# user_age = int(input('How old are you? '))

# if user_age >= 16:                           # if these aren't booleans, they're auto converted to booleans
#   print('You are old enough to drive!')
# else:
#   print('You are NOT old enough to drive.')

### Truthy and Falsy ###

# generally, if something has a value, it is considered Truthy
# for exammple: non-zero int, non-empty string, non-empty data structures
# things are generally considered Falsy if they are zero or empty

# invalid = True
# while invalid:

#   username = input('Enter a username: ')
#   password = input('Enter a password: ')
#   print()

#   if username and password:
#     hidden_password = '*' * len(password)
#     invalid = False
#     print(f'Hi {username}, your password is: {hidden_password}\n')

#   elif username and (not password):
#     print(f'Hi {username}, you need a valid password.\n')

#   elif (not username) and password:
#     print(f'Hi there, you need a username.\n')

#   else:
#     print(f'Hi there, you need a username and a password.\n')

# print(f'Username: {username}')
# print(f'Password: {hidden_password}')

### Ternary Operator ###

# condition_if_true if condition else condition_if_else

# is_friend = False
# can_message = 'message allowed' if is_friend else "not allowed to message"
# print(can_message)

### Short Circuiting ###

# is_Friend = True
# is_User = True

# print(is_friend or is_user) # if the first thing is true, the python interpreter just skips to the operation
# # works the same with the first being False in AND

### Logical operators ###

# == checks for equality in value
# is checks for whether things are pointing to the same memory

### For Loops ###

# for item in 'Zero to Mastery': # string
#   print(item)
# for item in [1,2,3,4,5]: # list
#   print(item)
# for item in (1,2,3,4,5): # tuple
#   print(item)

# user = {
#   'name': "TroyBoi",
#   'age': 29,
#   'can_swim': True
# }

# # the following are used EXTENSIVELY
# for item in user.items(): # key: value pairs as tuple
#   print(item)
# for item in user.values(): # values only
#   print(item)
# for item in user.keys(): # keys only
#   print(item)

# for key, value in user.items(): # not a tuple, keeps types of each
#   print(key, value)             # VERY COMMON

# for n in range(100):
#   print(n)

# for n in range(0, 100):
#   print(n)

# for n in range(60, 100): # start at first value, stop before second value
#   print(n)

# for _ in range(10): # common way to have something happen a certain number of times
#   print(_)

# for _ in range(0, 10, 2): # third value is step over
#   print(_)

# for _ in range(10, 0, -1): # to go in reverse
#   print(_)

# for _ in range(10, 0, -1): # creates a list of values  of a certain range
#   print(list(range(10)))

# enumerate: super useful if you need the index of things as you loop through, just like i in C++

# for i, value in enumerate('Hellooooo'): # i gives you the index and char give the value found there
#   print(i, value)

### While Loops ###

# i = 0
# while i < 50:
#   print(i)
#   i += 1
# else: # only runs after the while loop completes
#   print('Job\'s done')

# i = 0
# while i < 50:
#   print(i)
#   i += 1
#   break # breaks past the else statement; less common but good to know
# else:
#   print('Job\'s done')

# When to use a FOR loop vs. WHILE loop

# when looping over an iterable or a specific number of times, go with FOR loop
# when you don't know how many times something will loop, use a WHILE loop

# while True:
#   comment = input('Say something: ')
#   if comment == '':
#     print('You didn\' say anything.')
#   else:
#     break

# break, continue, pass
# break exits the loop that it is in
# continue skips everything after it and goes to the beginning of the loop
# pass is a placeholder that will avoid errors while you haven't written out a function or loop

### Functions: DRY ###

# def say_hello():
#   print('Hello')

# say_hello()

# Arguments are used to call a function and Parameters are used to define a function

# def say_hello(name, emoji): # these are positional because they are required to be in the proper position
#   print(f'Hello, {name} {emoji}')

# say_hello('Troy', ':)')

# # keyword arguments, generally bad practice because it can lead to confusion

# say_hello(emoji='butt', name='my')

# # Default Parameters can be declared in a function definition

# def say_hey(name='Darth Vader', emoji='BIG BUTT'):
#   print(f'Hello, {name} {emoji}')

# say_hey()

# Functions should do one thing really well, and only do that one thing
# Functions should usually return something

# Methods vs. Functions #
# methods are owns by objects
# functions can be used by anything

# Docstrings show up as hints when you are calling a function, use help(), or test.__doc__

# def test():
#   '''
#   Hey there buddy!
#   '''

### Clean Code ###

# def is_even(num): # not very clean
#   if num % 2 == 0:
#     return True
#   else:
#     return False

# def is_odd(num): # SO CLEAN
#   return num % 2 != 0

### *args and **kwargs ###

# def super_func(*args, **kwargs): # these can be anything, but this is the standard
#   print(*args) # returns each one individually
#   print(args) # returns a tuple of all arguments
#   print(kwargs) # returns a dictionary with keywords as keys and values as values
#   total = 0
#   for items in kwargs.values():
#     total += items
#   return sum(args) + total

# print(super_func(1,2,3,4,5, num1=5, num2=10))

# RULES of ordering: params, *args, default params, **kwargs

### Walrus operator := ###

# a = 'helloooooooooooo'
# if (n := len(a)) > 10: # walrus operator is assigning n the value of len(a) for this scope, kinda like int i = 0 in C/C++
#   print(f'too long, {n} elements')

# status = 'hungry'
# while ((n := len(status)) > 0): # checked and reassigned every loop
#   print(n)
#   status = status[:-1] # reassigns the value of status

### Scope ###

# defining functions creates a new scope that has access to itself
# interpreter starts with checking local, then checks the parent local up to global, and then built-ins

# parameters are local variables

# total = 0

# def count():
#   global total
#   total += 1
#   return total

# count()
# count()
# count()
# print(count())
