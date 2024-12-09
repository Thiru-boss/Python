Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> True+True
2
>>> True-False
1
>>> True-'hi'
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    True-'hi'
TypeError: unsupported operand type(s) for -: 'bool' and 'str'
>>> True*'Hi'
'Hi'
>>> False*'Hi'
''
