#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Garfield', 45)
cat2 = Cat('Tom', 22)
cat3 = Cat('Mr. Whiskers', 46)

# 2 Create a function that finds the oldest cat
cat_list = [cat1, cat2, cat3]
def find_oldest_cat(cats):
    oldest_cat = cats[0]  # initialize to first cat in the list
    for cat in cats:
        if cat.age > oldest_cat.age:
            oldest_cat = cat
    return oldest_cat

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {find_oldest_cat(cat_list).age} years old')