Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#join()
a='python','java','c'
''.join(a)
'pythonjavac'
' '.join(a)
'python java c'
a.join()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a.join()
AttributeError: 'tuple' object has no attribute 'join'
#formatting
a=5
b=8
print(a+b)
13
print("sum:",a+b)
sum: 13
a='pooja'
print('name:',a)
name: pooja
a='java'
print('the course is:,b')
the course is:,b
#concatenation
a='python'
b='course'
print(a+b)
pythoncourse
print(a+' '+b)
python course
print(a.title()+' '+b.title())
Python Course
print(a+b).title()
pythoncourse
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(a+b).title()
AttributeError: 'NoneType' object has no attribute 'title'
print((a+b).title())
Pythoncourse
print((a+' '+b).title())
Python Course
print((a+''+b).title())
Pythoncourse
#format method()
a='rupesh'
b='rupa'
print('helo'{}{}.format())
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('helo{}{}'.format())
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print('helo{}{}'.format())
IndexError: Replacement index 0 out of range for positional args tuple
print('helo{}{}'.format(a,b))
helorupeshrupa
print('helo{} {}'.format(a,b))
helorupesh rupa
print('helo {} {}'.format(a,b))
helo rupesh rupa
print('helo {} helo {}'.format(a,b))
helo rupesh helo rupa
print('helo {}\n helo {}\n'.format(a,b))
helo rupesh
 helo rupa

print('helo {a}\n helo {b}\n'.format(a,b))
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print('helo {a}\n helo {b}\n'.format(a,b))
KeyError: 'a'
print('helo {a}\n helo {b}\n'.format())
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print('helo {a}\n helo {b}\n'.format())
KeyError: 'a'
#fstring
a='rosie'
b='rupesh'
print(f'hello {a}{b}')
hello rosierupesh
print(f'hello {a}  {b}')
hello rosie  rupesh
print(f'hello {a} helo {b}')
hello rosie helo rupesh
hello rosie helo rupesh
SyntaxError: invalid syntax
a=5
b=6
print({}{}.format(a*b))
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('{}{}'.format(a*b))
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    print('{}{}'.format(a*b))
IndexError: Replacement index 1 out of range for positional args tuple
a=5
b=5
c=a*b
print('multiplication {}{}'.format(c))
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    print('multiplication {}{}'.format(c))
IndexError: Replacement index 1 out of range for positional args tuple
print('multiplication {}*{}'.format(c))
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    print('multiplication {}*{}'.format(c))
IndexError: Replacement index 1 out of range for positional args tuple
a=5
b=6
print('the product is {}'.format(a*b))
the product is 30
print(f'the product is {a*b}')
the product is 30
c=a*b
print('the product is {}'.format(c))
the product is 30
print(f'the product is {c}')
the product is 30
a='i am in class'
a[8]+a[9]+a[10]+a[11]+a[12]
'class'
a[5]+a[6]
'in'
a[2]+a[3]
'am'
a[1]+a[4]+a[7]
'   '
a='vijayawada is a royal city'
a[16]+a[17]+a[18]+a[19]+a[20]
'royal'
a[22]+a[23]+a[24]+a[25]
'city'
a[12]+a[13]
's '
a[11]+a[12]
'is'
b='vizag is a city of destiny'
a[11]+a[12]+a[13]+a[14]
'is a'
b[11]+b[12]+b[13]+b[14]
'city'
b[19]+b[20]+b[21]+b[22]b[23]+b[24]+b[25]
SyntaxError: invalid syntax
b[19]+b[20]+b[21]+b[22]+b[23]+b[24]+b[25]
'destiny'
b[0]+b[1]+b[2]+b[3]
'viza'
b[0]+b[1]+b[2]+b[3]+b[4]
'vizag'
a=' i am in python class'
a[-20]+a[-19]+a[-18]+a[-17]+a[-16]
'i am '
a[-7]+a[-8]+a[-9]+a[-10]+a[-11]+a[-20]
'nohtyi'
a[-1]+a[-2]+a[-3]+a[-4]+a[-5]

'ssalc'
a[-12]+a[-13]+a[-14]+a[-15]+a[-16]+a[-17]
'p ni m'
a[-12]+a[-11]+a[-10]+a[-9]+a[-8]+a[-7]
'python'
a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'class'
a[-18]+a[-17]
'am'
b='simple is better than complex'
a='simple is better than complex'
a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'complex'
a[-19]+a[-18]+a[-17]+a[-16]+a[-15]+a[-14]
'better'
#slicing
a='codegnan'
a[0:4]
'code'
>>> a{4:8}
SyntaxError: invalid syntax
>>> a[4:8]
'gnan'
>>> a[:4]
'code'
>>> a[4:]
'gnan'
>>> a='work until you succed'
>>> a[5:11]
'until '
>>> a[0:4]
'work'
>>> a[12:15]
'ou '
>>> a[11:15]
'you '
>>> a[16:22]
'ucced'
>>> a[15:22]
'succed'
>>> a='codegnan it solutions'
>>> a[4:9]
'gnan '
>>> a[9:11]
'it'
>>> a[12:20]
'solution'
>>> a[12:21]
'solutions'
>>> a='i am learning python'
>>> a[-15:-11]
'lear'
>>> a[-15:-10]
'learn'
>>> a[-6:-1]
'pytho'
>>> a[-6]
'p'
>>> a[-6:]
'python'
>>> b='i love python'
>>> b[-11:-7]
'love'
>>> b[-6:]
'python'
