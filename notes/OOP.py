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


# class PlayerCharacter:  # singular

#     # Class object attributes, same for all objects of this class, defined outside constructor
#     membership = True

#     # self refers to that instantiation (player1 or player2)
#     def __init__(self, name='NoName', age=0):
#         if (PlayerCharacter.membership == True):
#             self.name = name  # attributes are defined within the constructor
#             self.age = age

#     def run(self):  # all methods must use self as the first parameter
#         print('run')

#     def shout(self):
#         print(f'Hi, my name is {self.name}')

#     # Class Methods tagged like this can be used outside of an instantiation
#     # cls stands for Class and allows you to instantiate
#     @classmethod
#     def adding_stuff(cls, *args):
#         return cls('Buddy', sum(args))

#     # static methods don't give access to the class
#     @staticmethod
#     def adding_stuff2(*args):
#         return sum(args)


# player1 = PlayerCharacter('Joe', 45)
# player2 = PlayerCharacter('Troy', 29)

# # you can add attributes as you like, but they aren't given to all instantiations
# player2.attack = 50

# print(player1.name)
# print(player1.age)
# print(player2.name)
# print(player2.age)
# print(player2.attack)
# print(player1.membership)
# player1.shout()
# player2.shout()

# # because nothing was passed, defaults in the constructor are used
# player3 = PlayerCharacter()
# print(player3.name, player3.age)

# # you can instantiate with classmethods if you use cls
# player4 = PlayerCharacter.adding_stuff(1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(player4.age, player4.name)
# print(PlayerCharacter.adding_stuff2(3, 2, 3, 4, 2, 3, 4, 5))

# 4 Pillars of OOP
'''
1. Encapsulation - encapsulating attributes and methods (classes)
    - packaging things to help mimic the real world

2. Abstraction 
    - hide things that users don't need to worry about
    - functions should be intuitive and abstract away the "how"
    - public vs private
        - if you want something private, you put an underscore in front of it
        - this is only a convention; python doesn't actually have public and private
'''

'''
3. Inheritance
'''


class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')

# Inheritance is easy!


class Wizard(User):
    def __init__(self, name='NoName', power='NoPower', email='NoEmail'):
        User.__init__(self, email)  # this works, but isn't super clean
        self.name = name
        self.power = power

    def attack(self):
        print(f'{self.name} is attacking with {self.power}')


# Inheritance is easy!
class Archer(User):
    def __init__(self, name='NoName', num_arrows=0, email='NoEmail'):
        super().__init__(email)  # goes to the super class, meaning the one above it
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        # User.attack()  # this would allow you to call a parent class' function of same name
        self.num_arrows -= 1
        print(f'{self.name} is attacking with arrows: arrows left =  {self.num_arrows}')


wizard1 = Wizard('Merlin', 'fire', 'merlin@gmail.com')
archer1 = Archer('Robin Hood', 40, 'robinhood@gmail.com')
wizard1.sign_in()
archer1.sign_in()
wizard1.attack()
archer1.attack()

# check to see if something is an instance of an object type
print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
print(isinstance(wizard1, object))

'''
4. Polymorphism
    - different subclasses can share method names with different outputs
'''

# this is a great example of why polymorphism exists
# there might be multiple classes that inherit, but do different things
# both the wizard and the archer attack, but they do it in different ways
def player_attack(character):
    character.attack()


def print_email(character):
    print(character.email)


# these use their own class' attack functions even though they are called by the same function
player_attack(wizard1)
player_attack(archer1)
print_email(wizard1)
print_email(archer1)

# introspection
# print(dir(wizard1))  # allows you to see all of the methods available for an object

# Dunder Methods


class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'yoyo',
            'has_pets': False
        }

    def __str__(self):
        return f'{self.color}'  # only modifies str for objects of this class

    def __call__(self):  # modifies what happens when you "call" an object
        return ('yess??')

    def __getitem__(self, i):  # modifies what happens when you index an object
        return self.my_dict[i]


action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))
print(str('action_figure'))
print(action_figure())  # modified by the __call__ modification
print(action_figure['name'])  # modified by the __getitem__ modification


'''
Multiple inheritance: very powerful, but adds complexity
    - you can inherit from multiple classes:
class Hybrd(Archer, Wizard):

    - you have to be careful because you have to make sure things don't get tangled
'''

# Method Resolution Order


class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


print(D.num)
print(D.mro())
