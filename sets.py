Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

print('Hi'*3)
HiHiHi

#sets{}
a={1,2.2,"Hi",5+4j,True}
a
{(5+4j), 'Hi', 2.2, 1}
type(a)
<class 'set'>
a={1,2,3,2,4,5,2,6,9}
a
{1, 2, 3, 4, 5, 6, 9}

#....issubset()....#
a={1,2,3,4,5,6,7,8,9}
b={3,4,5}
b.issubset(a)
True
a.issuset(b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.issuset(b)
AttributeError: 'set' object has no attribute 'issuset'. Did you mean: 'issubset'?
a.issubset(b)
False

#....issuperset()....#
b.issuperset(a)
False
a.issuperset(b)
True

#....add()....#
a.add(10)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
b.add({11,12})
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    b.add({11,12})
TypeError: cannot use 'set' as a set element (unhashable type: 'set')
b.add(11)
b.add(12)

#......union().....#
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

b.union(a)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

#....intersection()....#
a.intersection(b)
{3, 4, 5}
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

#....update()....#
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

#...difference().....#
a={1,2,3,4,5}
b={3,4,5,6}
a.difference(b)
{1, 2}
b.difference(a)
{6}

#.....symmetric_differnce()....#
a={1,2,3,4,5,6,7,8}
b={6,7,8,9,10}
a.symmetric_difference(a)
set()
a.symmertic_difference(b)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a.symmertic_difference(b)
AttributeError: 'set' object has no attribute 'symmertic_difference'. Did you mean: 'symmetric_difference'?
a.symmetric_difference(b)
{1, 2, 3, 4, 5, 9, 10}
b.symmetric_difference(a)
{1, 2, 3, 4, 5, 9, 10}

#....difference_update()....#
a.difference_update(b)
a
{1, 2, 3, 4, 5}
b.difference_update(a)
b
{6, 7, 8, 9, 10}

a={4,5,6,7,8,9}
b={1,2,3,4,5,6}
a.intersection_update(b)
a
{4, 5, 6}
b.intersection_update(a)
b
{4, 5, 6}

a={1,2,3,4,5,6}
b={4,5,6,7,8}
a.symmetric_update(b)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    a.symmetric_update(b)
AttributeError: 'set' object has no attribute 'symmetric_update'
a.symmetric_difference_update(b)
a
{1, 2, 3, 7, 8}
b.symmetric_difference_update(a)
b
{1, 2, 3, 4, 5, 6}


a={10,20,30,40,50}
a.copy()
{50, 20, 40, 10, 30}
a.clear()
a
set()
b=set()
a.add(10)
b.add(90)
b
{90}

a={7,8,9,10,1,11}
a
{1, 7, 8, 9, 10, 11}
a.pop()
1
a.remove(10)
a
{7, 8, 9, 11}

a={1,2,3,4,5}
a.discard(4)
a
{1, 2, 3, 5}
b={4,5,6,7}
c={1,2,3,4}
b.discard(c)
b
{4, 5, 6, 7}
c
{1, 2, 3, 4}


len(a)
4
a.count(8)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    a.count(8)
AttributeError: 'set' object has no attribute 'count'
a.index(7)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    a.index(7)
AttributeError: 'set' object has no attribute 'index'
>>> 
>>> a={4,5,6,7,8}
>>> b={7,8,9,10}
>>> a.disjoint(b)
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    a.disjoint(b)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
>>> a.isdisjoint(b)
False
>>> 
>>> a={1,2,3,4}
>>> b={5,6,7,8}
>>> a.isdisjoint(b)
True
>>> 
>>> a={6,7}
>>> 
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> a1=a[0:5]
>>> a1
[9, 1, 5, 2, 8]
>>> a2=[5:10]
SyntaxError: invalid syntax
>>> a2=a1[5:10]
>>> a2
[]
>>> a1.sort()
>>> a1
[1, 2, 5, 8, 9]
>>> a2.sort()
>>> a2
[]
>>> a2=a[5:10]
>>> a2.sort()
>>> a2
[0, 3, 4, 6, 7]
>>> a2.reverse()
>>> a2
[7, 6, 4, 3, 0]
>>> a1.reverse()
>>> a1+a2
[9, 8, 5, 2, 1, 7, 6, 4, 3, 0]
>>> a2+a1
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
