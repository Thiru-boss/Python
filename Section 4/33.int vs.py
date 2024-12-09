Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
10+4
14
10-4
6
10*4
40
10/4
2.5
10//4
2
10%4
2
10**4
10000
10+1.5
11.5
>>> 10-1.5
8.5
>>> 10*1.5
15.0
>>> 10/1.5
6.666666666666667
>>> 10//1.5
6.0
>>> 10%1.5
1.0
>>> 10**1.5
31.622776601683793
>>> 10+true
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    10+true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> 10+True
11
>>> 10-False
10
>>> 10+(5+2j)
(15+2j)
>>> 10-(5+2j)
(5-2j)
>>> 10*(5+2j)
(50+20j)
>>> 10/(5+2j)
(1.7241379310344829-0.6896551724137931j)
>>> 10//(5+2j)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    10//(5+2j)
TypeError: unsupported operand type(s) for //: 'int' and 'complex'
>>> 10**(5+2j)
(-10701.348355876977-99425.75694137898j)
>>> 2*'Hi'
'HiHi'
