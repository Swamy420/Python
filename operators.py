Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#operators
#arthematic
a,b=2,2
a+b
4
b-a
0
a*b
4
a//b
1
a/b
1.0
a%b
0
a**b
4

#assignment
a=10,b=20
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a,b=10,20
b+=a
b
30
b-=10
b
20
a*=b
a=
SyntaxError: invalid syntax
a
200
b**=2
b
400
b//=100
b
4
a/=89
a
2.247191011235955
a%=b
a
2.247191011235955
b%=a
b
1.7528089887640448

#comparision
a,b=10,9
a<b
False
a>b
True
b<a
True
b>a
False
a<=b
False
a>=b
True
b<=a
True
b>=a
False
b==a
False
a!=b
True

#Logical
a>b && b<a
SyntaxError: invalid syntax
a>b and b<a
True
a>=b and a<=a
True
a!=b and a==b
False
>>> a>b or  b>a
True
>>> a<b or b<a
True
>>> a!=b or a==b
True
>>> not True
False
>>> not False
True
>>> 
>>> #Identifr
>>> #Identifr
>>> #Identify
>>> a=12
>>> if type(a) is int:
...     a
... 
12
>>> if type(a) is not int:
...     a
... else:
...     print("hello")
... 
...     
hello
>>> 
>>> 
>>> #Membership
>>> a=1,2,3,4,5
>>> if 2 in a:
...     print(2)
... else:
... 
...     a
... 
...     
2
>>> if 7 not in a:
...     print(a)
... else:
...     print(7)
... 
...     
(1, 2, 3, 4, 5)
