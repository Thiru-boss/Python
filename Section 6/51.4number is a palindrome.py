n = int(input('Enter a number'))
n = n
rev = 0
while n > 0:
    r = n % 10
    n = n // 10
    rev = rev * 10 + r
if n == rev:
 print('Number is a palindrome')
else:
    print('Number is not a palindrome')
