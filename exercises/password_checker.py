# take input from the user for both the username and password,
# then print a message that tells them how long their password
# is without showing the actual password

username = input('Enter a username: ')
password = input('Enter a password: ')

password_length = len(password)
password_placeholder = '*' * password_length

print(f'{username}, your password {password_placeholder} is {password_length} characters long')