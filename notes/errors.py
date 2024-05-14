# Error Handling

while True:
    try:
        age = int(input('How old are you? '))
        10/age
    except ValueError:
        print('Please enter an integer\n')
    except ZeroDivisionError:
        print('Can\'t divide by zero\n')
    else:
        break

print()

