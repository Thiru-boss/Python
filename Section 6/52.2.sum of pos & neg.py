num_of_nos = int(input('Enter number of number'))
Psum = 0
Nsum = 0
count = 0

while count < num_of_nos:
    n = int(input('Enter number of number'))
    if n > 0:
        Psum = Psum + n

else:
    Nsum = Nsum + n
    count = count + 1
print('Positive sum is ', Psum)
print('Negative sum is ', Nsum) 