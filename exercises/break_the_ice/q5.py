# Define a class which has at least two methods:

# getString: to get a string from console input
# printString: to print the string in upper case.

# Also please include simple test function to test the class methods.

class MyClass():

    def __init__(self):
        self.s = ''

    def get_string(self):
        self.s = input('Enter a string:\n')

    def print_string(self):
        print('Your string:')
        print(self.s)

string_obj = MyClass()
string_obj.get_string()
string_obj.print_string()
