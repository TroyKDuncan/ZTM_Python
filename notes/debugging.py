# debugging - senior devs are REALLY good at debugging

# tips

# use linting
# use an ide or editor
# learn to read errors (become familiar with the most common errors)
# if you see an error that you don't recognize, go read about it in the documentation
# pdb - The Python Debugger

import pdb  # super dope for CLI debugging, but you can always just use the vscode db


def sum(*args, **kwargs):
    total = 0
    pdb.set_trace()
    for num in args:
        total += num
    return total


print(sum(1, 2, 3, 'a'))
