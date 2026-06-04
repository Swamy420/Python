Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a={"name":"Gopi","year":2026,"month":"june"}
a
{'name': 'Gopi', 'year': 2026, 'month': 'june'}
type(a)
<class 'dict'>
a.keys()
dict_keys(['name', 'year', 'month'])
a.values()
dict_values(['Gopi', 2026, 'june'])


a={'city':'vja','country':'India','state':'ap'}
a
{'city': 'vja', 'country': 'India', 'state': 'ap'}
a.update({'state':'ap'},{'district':'NTR'})
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a.update({'state':'ap'},{'district':'NTR'})
TypeError: update expected at most 1 argument, got 2
a.update({'state':'ap','district':'NTR'})
a
{'city': 'vja', 'country': 'India', 'state': 'ap', 'district': 'NTR'}
a.update({'state':'ts','district':'xy'})
a
{'city': 'vja', 'country': 'India', 'state': 'ts', 'district': 'xy'}
a.update({'state':'ap','district':'NTR'})
aa
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    aa
NameError: name 'aa' is not defined. Did you mean: 'a'?
a
{'city': 'vja', 'country': 'India', 'state': 'ap', 'district': 'NTR'}


a={'day':'thursday','date':4}
a
{'day': 'thursday', 'date': 4}
a.setdefault('time',10)
10
a
{'day': 'thursday', 'date': 4, 'time': 10}


a={'name':'Gopi','mail':'example@gmail.com'}
a.get(mail)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a.get(mail)
NameError: name 'mail' is not defined
a.get('mail')
'example@gmail.com'
a
{'name': 'Gopi', 'mail': 'example@gmail.com'}
a['name']
'Gopi'
a['Gopi']
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a['Gopi']
KeyError: 'Gopi'
a.get('Gopi')
a
{'name': 'Gopi', 'mail': 'example@gmail.com'}


a={'name':'Gopi','mail':'example@gmail.com','city':'vja','mobile':91919}
a
{'name': 'Gopi', 'mail': 'example@gmail.com', 'city': 'vja', 'mobile': 91919}
a.pop()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop('mobile')
91919
a
{'name': 'Gopi', 'mail': 'example@gmail.com', 'city': 'vja'}
>>> a.popitem()
('city', 'vja')
>>> 
>>> 
>>> a={'name':'Gopi','mail':'example@gmail.com','city':'vja','mobile':91919}
... a.copy()
SyntaxError: multiple statements found while compiling a single statement
>>> b={'name':'Gopi','mail':'example@gmail.com','city':'vja','mobile':91919}
... b.copy()
SyntaxError: multiple statements found while compiling a single statement
>>> a={"name":"Gopi","year":2026,"month":"june"}
>>> a.copy()
{'name': 'Gopi', 'year': 2026, 'month': 'june'}
>>> 
>>> 
>>> 
>>> a={'name':'Gopi','mail':'example@gmail.com','city':'vja','name':'Gopi'}
>>> a
{'name': 'Gopi', 'mail': 'example@gmail.com', 'city': 'vja'}
>>> 
... a={'name':'Gopi','mail':'example@gmail.com','city':'vja','name':'swamy'}
>>> a
{'name': 'swamy', 'mail': 'example@gmail.com', 'city': 'vja'}
>>> 
... a={'name':'Gopi','mail':'example@gmail.com','city':'vja','name1':'Gopi'}
>>> a
{'name': 'Gopi', 'mail': 'example@gmail.com', 'city': 'vja', 'name1': 'Gopi'}
>>> 
>>> len(a)
4
>>> a.clear()
>>> a
{}
>>> 
>>> 
>>> a={'id':[10,20,30],'names':['x','y','z'],'marks':[90,90,90]}
>>> a
{'id': [10, 20, 30], 'names': ['x', 'y', 'z'], 'marks': [90, 90, 90]}
>>> type(a)
<class 'dict'>
>>> a.keys()
dict_keys(['id', 'names', 'marks'])
>>> a.values()
dict_values([[10, 20, 30], ['x', 'y', 'z'], [90, 90, 90]])
>>> a.items()
dict_items([('id', [10, 20, 30]), ('names', ['x', 'y', 'z']), ('marks', [90, 90, 90])])
