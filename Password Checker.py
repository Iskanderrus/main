username = input('Enter your Username: ')
password = input('Enter your password: ')
print(f'Hi, {username}! Your password ' + ('*' * len(password)) + ' is ', len(password), ' letters long')