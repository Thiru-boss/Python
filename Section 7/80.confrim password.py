pass1 = input('Enter password')
pass2 = input('Enter password')
if pass1 == pass2:
    print('Password is correct')
else:
    if pass1.casefold() == pass2.casefold():
        print('please check for the casses and try again')
    print('password is worng')