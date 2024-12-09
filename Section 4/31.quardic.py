Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> a = int(input('enter a value'))
enter a value1
>>> b = int(input('enter a value'))
enter a value-4
>>> c= int(input('enter a value'))
enter a value4
>>> root1 = (-b + math.sqrt(b ** 2 - 4 * a * c))/(2*a)
>>> root1 = (-b - math.sqrt(b ** 2 - 4 * a * c))/(2*a)
>>> print('roote are', root1,root2)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print('roote are', root1,root2)
NameError: name 'root2' is not defined. Did you mean: 'root1'?
>>> print('roots are', root1,root2')
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print('root are', root1,root2)
...       
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print('root are', root1,root2)
NameError: name 'root2' is not defined. Did you mean: 'root1'?
>>> root2 = (-b - math.sqrt(b ** 2 - 4 * a * c))/(2*a)
...       
>>> print('root are', root1,root2)
...       
root are 2.0 2.0
