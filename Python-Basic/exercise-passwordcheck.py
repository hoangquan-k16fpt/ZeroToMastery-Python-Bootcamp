username = input('What is your username? ')
password = input('What is your password? ')

password_length = len(password)
hidden_password = '*' * password_length

print(f'Hello {username}. Your password is {hidden_password} has {password_length} characters long.')
