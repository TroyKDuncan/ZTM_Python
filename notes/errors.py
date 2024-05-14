# Error Handling

while True:
    try:
        age = int(input('How old are you? '))
        10/age
    except ValueError:  # best practice is to catch specific errors
        print('Please enter an integer\n')
    except ZeroDivisionError:
        print('Can\'t divide by zero\n')
    else:
        break
print()

# TypeError as err: err is an object that can be printed as a decription


def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:  #
        print(f'please enter numbers: {err}')


print(sum(1, '2'))
print()


# handle multiple errors the same way
def div(num1, num2):
    try:
        return num1/num2
    except (TypeError, ZeroDivisionError):
        print('Oopsie daisy')


div(1, '2')
div(1, 0)
print()


def div(num1, num2):
    try:
        return num1/num2
    except (TypeError, ZeroDivisionError) as err:  # handle multiple errors the same way
        print(err)  # this will just print out which error is being thrown


div(1, '2')
div(1, 0)
print()


# finally runs at the end of EVERY iteration, whether is successful or not
while True:
    try:
        age = int(input('How old are you? '))
        10/age
    except ValueError:
        print('Please enter an integer\n')
    except ZeroDivisionError:
        print('Can\'t divide by zero\n')
    else:
        print('Thanks!')
        break
    finally: 
        print('Job\'s done')
print()


# you can raise your own warnings
# errors are unavoidable, but it is up to YOU to decide how they are handled and anticipate issues
while True:
    try:
        age = int(input('How old are you? '))
        10/age
        raise ValueError('Can\'t milk those!')
    except ZeroDivisionError:
        print('Can\'t divide by zero\n')
        break
    else:
        print('Thanks!')
    finally: 
        print('Job\'s done')
print()
