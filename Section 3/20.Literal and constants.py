Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=123_345
>>> a
123345
>>> b=1_2
>>> b
12
>>> f=123_45.66
>>> f
12345.66
>>> f=12_23
>>> f
1223
>>> f=_12
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    f=_12
NameError: name '_12' is not defined
>>> f=123_.45
SyntaxError: invalid decimal literal
>>> f=1_2.4_5
>>> f
12.45
>>> c=5_4+1_2)
SyntaxError: unmatched ')'
>>> c=5_4+1_2j
>>> c
(54+12j)
>>> name'john'
SyntaxError: invalid syntax
>>> name='john'
>>> name
'john'
>>> name="john"
>>> name
'john'
>>> price=input("nterprice")
nterprice123
>>> price
'123'
