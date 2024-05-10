# OOP is a paradigm

class BigObject:  # camel case convention
    pass


obj1 = BigObject()
print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('hey'))
print(type([]))
print(type(()))
print(type({}))
print(type(obj1))


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

    # Class Methods tagged like this can be used outside of an instantiation
    # cls stands for Class and allows you to instantiate
    @classmethod
    def adding_stuff(cls, *args):
        return cls('Buddy', sum(args))

    # static methods don't give access to the class
    @staticmethod
    def adding_stuff2(*args):
        return sum(args)


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

# you can instantiate with classmethods if you use cls
player4 = PlayerCharacter.adding_stuff(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(player4.age, player4.name)
print(PlayerCharacter.adding_stuff2(3, 2, 3, 4, 2, 3, 4, 5))
