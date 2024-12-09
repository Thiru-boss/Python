Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=True
a
True
int(a)
1
>>> type(a)
<class 'bool'>
>>> b=False
>>> b
False
>>> int(b)
0
>>> type(b)
<class 'bool'>
>>> int(False)
0
>>> int(true)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> int(True)
1
>>> complex
<class 'complex'>
>>> x=3+5j
>>> type(x)
<class 'complex'>
>>> a=1.22+3.55j
>>> a
(1.22+3.55j)
>>> b=complex(12,9)
>>> b
(12+9j)
>>> c=complex(12)
>>> c
(12+0j)
>>> a.mag
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.mag
AttributeError: 'complex' object has no attribute 'mag'. Did you mean: 'imag'?
>>> a.imag
3.55
