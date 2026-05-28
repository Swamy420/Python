Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name="hi"
print(name)
hi
print("hi")
hi
place="vja"
print(place)
vja
country="India"
print(country)
India
#special character and underscore
!=20
SyntaxError: invalid syntax
^=20
SyntaxError: invalid syntax
_=30
print(_)
30
_a=9
print(-a)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(-a)
NameError: name 'a' is not defined. Did you mean: '_a'?
print(_a)
9
 x=100
 
SyntaxError: unexpected indent
_100
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    _100
NameError: name '_100' is not defined
India
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    India
NameError: name 'India' is not defined
India
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    India
NameError: name 'India' is not defined


#keywords
if=30
SyntaxError: invalid syntax
else=3
SyntaxError: invalid syntax


#single line multiple values
a=3,b=9
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=1;b=2
print(a,b)
1 2
print(a+b)
3
a,b=6,7
print(a+b)
13
a=3,4,5,6,7
print(a)
(3, 4, 5, 6, 7)


#multiple values have single variable and single variable have multiple values
a=b=c=20
print(a,b,c)
20 20 20
a,b,c=3,4,5,6
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a,b,c=3,4,5,6
ValueError: too many values to unpack (expected 3, got 4)
a,b,c=6,7,8
print(a,b,c)
6 7 8

>>> #space btw variable
>>> fi na="hi"
SyntaxError: invalid syntax
>>> fi_na="hi"
>>> print(fi_na)
hi
>>> 
>>> #concatenation
>>> la_na="ra"
>>> print(fi_na,la_na)
hi ra
>>> print(fi_na,+" ",+la_na)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    print(fi_na,+" ",+la_na)
TypeError: bad operand type for unary +: 'str'
>>> print(fi_na+" "+la_na)
hi ra
>>> 
>>> 
>>> #unpacking and delete
>>> a,b,c=(6,7,8)
>>> print(a,b,c)
6 7 8
>>> x=10
>>> print(x)
10
>>> del a
>>> del x
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined. Did you mean: '_a'?
>>> 
>>> 
>>> #case sensitive
>>> Age=10
>>> print(Age)
10
>>> AGE=20
>>> print(AGE)
20
>>> age=3
>>> print(age)
3
