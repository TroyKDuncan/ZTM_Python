# OOP is a paradigm

# class BigObject:  # camel case convention
#     pass


# obj1 = BigObject()
# print(type(None))
# print(type(True))
# print(type(5))
# print(type(5.5))
# print(type('hey'))
# print(type([]))
# print(type(()))
# print(type({}))
# print(type(obj1))

class PlayerCharacter:  # singular

    # Class object attributes, same for all objects of this class, defined outside constructor
    membership = True

    # self refers to that instantiation (player1 or player2)
    def __init__(self, name='NoName', age=0):
        if (PlayerCharacter.membership == True):
            self.name = name  # attributes are defined within the constructor
            self.age = age

    def run(self):  # all methods must use self as the first parameter
        print('run')

    def shout(self):
        print(f'Hi, my name is {self.name}')


player1 = PlayerCharacter('Joe', 45)
player2 = PlayerCharacter('Troy', 29)

# you can add attributes as you like, but they aren't given to all instantiations
player2.attack = 50

print(player1.name)
print(player1.age)
print(player2.name)
print(player2.age)
print(player2.attack)
print(player1.membership)
player1.shout()
player2.shout()

# because nothing was passed, defaults in the constructor are used
player3 = PlayerCharacter()
print(player3.name, player3.age)
