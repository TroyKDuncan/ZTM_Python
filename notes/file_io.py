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


with open('test.txt', mode='r+') as my_file:  # more common, r+ means read and write
    text = my_file.write('Hey gurrrrl')
    print(my_file.readlines())
