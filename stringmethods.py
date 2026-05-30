Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
#len()
a="hi"
len(a)
2
a="hiii jk"
len(a)
7
a=""
len(a)
0
a=" "
len(a)
1

#count()
a="hddfiindfdenfdv kldnvkjdsnvnb ffnwendff  jbfdjbfh b"
count(a)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count(d)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.count(d)
NameError: name 'd' is not defined. Did you mean: 'id'?
a.count("d")
9
a.count("ff")
2
a.count("t")
0
a.count(" ")
5

#find a string
a="Gopi swamy"
a.find("s")
5
a.find("i")
3

#escape sequences
#\n->new line
#\t->tab space
a="Gopi\nmailid:example@gmail.com\tmobile:9987654321
SyntaxError: unterminated string literal (detected at line 1)
a="Gopi\nmailid:example@gmail.com\tmobile:9987654321"
a
'Gopi\nmailid:example@gmail.com\tmobile:9987654321'
print(a)
Gopi
mailid:example@gmail.com	mobile:9987654321

#replace()

a="My name Gopi"
a.replace("Gopi","Swamy")
'My name Swamy'
a="My name is Gopi"
a.replace("Gopi","Swamy")
'My name is Swamy'
a="wait wait until you succeed"
a.replace("wait","work")
'work work until you succeed'
a.replace("wait","work",1)
'work wait until you succeed'

#uppercase
a="code"
a.upper()
'CODE'
#Lower case
a="CODE"
a.lower()
'code'
a.capitalize()
'Code'
a="gopi swamy"
a.title()
'Gopi Swamy'

a="hello"
a.isupper()
False
a.islower()
True
a.isdigit()
False
a='hello world'
a.isalph()
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    a.isalph()
AttributeError: 'str' object has no attribute 'isalph'. Did you mean: 'isalpha'?
>>> a.isalpha()
False
>>> a='helloworld'
>>> a.isalpha()
True
>>> a="2345"
>>> a.isdigit()
True
>>> 
>>> a="exa@123"
>>> a.isalnum()
False
>>> a="ex123"
>>> a.isalnum()
True
>>> a='joker'
>>> a.startswith('j')
True
>>> a.startswith('k')
False
>>> a.endswith('r')
True
>>> a.endswith('j')
False
>>> 
>>> #strip()
>>> #lstrip(),rstrip()
>>> a='     hello        '
>>> a.strip()
'hello'
>>> a.lstrip()
'hello        '
>>> a.rstrip()
'     hello'
>>> 
>>> #split()
>>> a="python java c c++"
>>> a.split()
['python', 'java', 'c', 'c++']
>>> a="pythonjavacc++"
>>> a.split()
['pythonjavacc++']
>>> a='i am learning python course'
>>> a.split()
['i', 'am', 'learning', 'python', 'course']
