# Create an @authenticated decorator that only allows the function to run if user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': False
}

user2 = {
    'name': 'Troy',
    # changing this will either run or not run the message_friends function.
    'valid': True
}


def authenticated(fn):
    def wrapper(*args,**kwargs):
        for user in args:
            print('For user ' + user['name'] + ':')
            if user['valid'] == True:
                fn(user)
                print()
            else:
                print('Invalid user')
                print()
    return wrapper



@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1, user2)
