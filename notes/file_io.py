# File I/O

my_file = open('test.txt')

print(my_file)
print(my_file.read())
print(my_file.read())
print(my_file.read())  # uses a cursor, so after the first read, you're at the end

my_file.seek(0)
print(my_file.read())
my_file.seek(0)
print(my_file.read())
my_file.seek(0)
print(my_file.read())  # uses a cursor, so after the first read, you're at the end
print()

my_file.seek(0)
print(my_file.readline())
print(my_file.readline())
my_file.seek(0)
print(my_file.readlines())

my_file.close()


with open('test.txt', mode='r+') as my_file:  # r+ means read and write
    # when in r+, write overwrites wherever the cursor is
    text = my_file.write('Hey gurrrrl')
    print(my_file.readlines())

# w means write, you can only write and it assumes the file is empty
with open('test.txt', mode='w') as my_file:
    # when in w, write assumes the file is
    text = my_file.write('Hey gurrrrl')

# w means write, you can only write and it assumes the file is empty
with open('happy.txt', mode='w') as my_file:
    # when in w, write assumes the file is
    text = my_file.write(':)')

# w allows you to create new files too
with open('sad.txt', mode='w') as my_file:
    text = my_file.write(':(')
    print(text)  # this prints the number of characters in the file

# a means append, so it adds things to the end of the file, still using the write function
with open('sad.txt', mode='a') as my_file:
    text = my_file.write(':(')

# CHECKOUT PATHLIB BUILT-IN