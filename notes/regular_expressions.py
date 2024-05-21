import re

my_string = 'search this inside of this text please'

print('search' in my_string)

a = re.search('this', my_string)  # returns a match object or None
print(a.span())
print(a.start())
print(a.end())
print(a.group())

# this is the pattern that is being searched for using the following commands
pattern = re.compile('search this')
b = pattern.search(my_string)  # return first instance
c = pattern.findall(my_string)  # returns a list of all instances
d = pattern.fullmatch(my_string)  # returns True or None
# this returns a match object if the beginning matches
e = pattern.match(my_string)
print(b)
print(c)
print(d)
print(e)

# Real world scenarios:

# Email validation:

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

# + after brackets means unlimited, then @, then unlimited for those brackets, then . then between 2-7 letters

pattern = re.compile(email_regex)
print(pattern.fullmatch('tkduncan614@gmail.com'))

# Password checker:

# at least 8 char long
# contain letters, numbers, $%#@
# ends with a number

password_regex = r'^[A-Za-z0-9$%#@]{8,}[0-9]$'
pattern2 = re.compile(password_regex)
print(pattern2.fullmatch('helloworLD#5'))