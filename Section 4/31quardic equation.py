import math
a = int(input('enter a value'))
b = int(input('enter a value'))
c = int(input('enter a value'))
root1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2*a)
root2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2*a)
print('roots are ', root1, root2)

