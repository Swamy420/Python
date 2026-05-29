Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #datatype conversions
>>> #integer
>>> int(1)
1
>>> int(4.1)
4
>>> int("ji")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("ji")
ValueError: invalid literal for int() with base 10: 'ji'
>>> int(1+8j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(1+8j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> int(True)
1
>>> int(False)
0
>>> 
>>> #float
>>> float(1)
1.0
>>> float(1.2)
1.2
>>> float("hi")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float("hi")
ValueError: could not convert string to float: 'hi'
>>> float(8+j)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float(8+j)
NameError: name 'j' is not defined
>>> float(True)
1.0
>>> float(False)
0.0
>>> 
>>> #string
>>> str(8)
'8'
>>> str(19)
'19'
str(19.8)
'19.8'
str(12+j)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    str(12+j)
NameError: name 'j' is not defined
str(1+2j)
'(1+2j)'
str(j)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    str(j)
NameError: name 'j' is not defined
str(True)
'True'
str(False)
'False'

#complex
complex(1)
(1+0j)
complex(1.2)
(1.2+0j)
complex(9+j)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    complex(9+j)
NameError: name 'j' is not defined
complex(9+1j)
(9+1j)
complex(True)
(1+0j)
complex(False)
0j

#boolean
bool(1)
True
bool(1.2)
True
bool(1+0j)
True
bool("True")
True
bool(True)
True
bool(False)
False
