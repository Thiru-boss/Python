n = int(input('Enter a number'))

count = 0

for i in range(1, n+1):
    if n % i == 0:
        count += 1

if count == 2:
    print('Its prime no')
else:
    print('Its not prime no')
