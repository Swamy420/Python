Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a='data science'
a[::]
'data science'
a[::1]
'data science'
a[::2]
'dt cec'
#striding
a='cloud computing'
a[::4]
'cdmi'
a[::3]
'cucpi'
a[::6]
'cci'
#slicing
a[3:6]
'ud '
a[:9]
'cloud com'
a[7:]
'omputing'
a='machine learning'
a[1:10:3]
'ai '
a[1:14:4]
'anei'
[2:14:4]
SyntaxError: invalid syntax
a[2:14:4]
'cea'
a[3:15:5]
'hli'
a[1:12:2]
'ahn er'
a='python course'
a[-1:-11-4]
''
a[-1:-11:-4]
'eoo'
a[-3:-13:-5]
'rn'
a[-5:-12:-6]
'ot'
a[-2:-9:-1]
'sruoc n'
a[-6:13:-3]
''
a[-6:-13:-3]
'coy'
a[-4:-12:-6]
'uh'


#list()
#list[]
a=[1,2.1,"c++",5+9j,False]
a
[1, 2.1, 'c++', (5+9j), False]
type(a)
<class 'list'>
b=8.9
type(b)
<class 'float'>
b=[9.1]
type(b)
<class 'list'>

a=["Python,C,C++"]
a.append("Java")
a
['Python,C,C++', 'Java']
a.append(['ml,ai'])
a
['Python,C,C++', 'Java', ['ml,ai']]

a.extend(['dsa','db'])
a
['Python,C,C++', 'Java', ['ml,ai'], 'dsa', 'db']

a=['black','white']
a.insert(0,'green']
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
a.insert(0,'green')
a
['green', 'black', 'white']
a.index("black")
1
a.copy()
['green', 'black', 'white']
b=a.copy()
b
['green', 'black', 'white']
a.sort()
a
['black', 'green', 'white']
b=[6,3,44,5]
b.sort()
b
[3, 5, 6, 44]
a.reverse()
a
['white', 'green', 'black']
b.reverse()
b
[44, 6, 5, 3]


a=["Python,C,C++"]
a.pop()
'Python,C,C++'
a
[]
a=['black','white']
a.pop()
'white'
a
['black']
a=['black','white']
a.pop(1)
'white'
a.pop(0)
'black'
a=['black','white']
a.remove('black')
a
['white']

a=['hi','hello','how']
len(a)
3
b='hello'
len(b)
5
c=['hello']
len(c)
1
a.count('how')
1

a=['python','java']
a.clear()
a
[]
b=[]
a.append('Gopi')
a
['Gopi']

#tuple()
a=(5,6.7,'python',8+9j,True)
len(a)
5
a
(5, 6.7, 'python', (8+9j), True)
type(a)
<class 'tuple'>
a.count(True)
1
a.index('8+9j)
        
SyntaxError: unterminated string literal (detected at line 1)
a.index(8+9j)
        
3
>>> a=[9,1,5,2,8,4,6,3,7,0]
...         
>>> b=a.reverse(5,:)
...         
SyntaxError: invalid syntax
>>> b=a.reverse([5,:])
...         
SyntaxError: invalid syntax
>>> mid=len(a//2)
...         
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    mid=len(a//2)
TypeError: unsupported operand type(s) for //: 'list' and 'int'
>>> mid=len(a)//2
...         
>>> b=a[mid:]
...         
>>> b.reverse()
...         
>>> c=a[:mid]
...         
>>> c.reverse()
...         
>>> b+=c.copy()
...         
>>> b
...         
[0, 7, 3, 6, 4, 8, 2, 5, 1, 9]
>>> a=[9,1,5,2,8,4,6,3,7,0]
...         
>>> mid=len(a)//2
...         
>>> b=a[mid:]
...         
>>> c=a[:mid-1]
...         
>>> c.reverse()
...         
>>> b.reverse()
...         
>>> c+=b
...         
>>> c
...         
[2, 5, 1, 9, 0, 7, 3, 6, 4]
