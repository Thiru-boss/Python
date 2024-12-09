cardno = input('Enter card no')
lastdigits = cardno[15::]
four = '*' * 4 + ' '
dispno = four * 3 + lastdigits
print(dispno)