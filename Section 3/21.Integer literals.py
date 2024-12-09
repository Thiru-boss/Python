Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> a
10
>>> a=0b1010
>>> a
10
>>> a=0xa
>>> a
10
>>> f=0b111.111
SyntaxError: invalid syntax
>>> c=4+6j
>>> c
(4+6j)
>>> c=0b101+6j
>>> c
(5+6j)
>>> c=5+0b110j
SyntaxError: invalid binary literal
>>> price=input("enter price")
enter price0b101
>>> price
'0b101'
>>> price=int(input('enter price'),2)
enter price0b101
>>> price
5
