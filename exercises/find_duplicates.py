# print out items that have duplicates

some_list = ['a','b','c','b','d','m','n','n']

duplicates = []
already_seen = []
for letter in some_list:
  if letter in already_seen:
    duplicates.append(letter)
  else:
    already_seen.append(letter)

print(duplicates)

# OR

duplicates = []
for letter in some_list:
  if some_list.count(letter) > 1:
    if letter not in duplicates:
      duplicates.append(letter)

print(duplicates)