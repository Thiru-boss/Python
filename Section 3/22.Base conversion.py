Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> b=16
>>> c=255
>>> bin(a)
'0b1010'
>>> bin(b)
'0b10000'
>>> bin(c)
'0b11111111'
>>> oct(a)
'0o12'
>>> oct(b)
'0o20'
>>> oct(c)
'0o377'
>>> hex(10)
'0xa'
>>> hex(16)
'0x10'
>>> hex(255)
'0xff'
>>> hex(true)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    hex(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> hex(True)
'0x1'
>>> bin(True)
'0b1'
