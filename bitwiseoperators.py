Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#bitwise operators
a,b=5,1
a&b
1
>>> bin(a)
'0b101'
>>> bin(b)
'0b1'
>>> a,b=10,10
>>> a&b
10
>>> a,b=5,2
>>> a&b
0
>>> bin(a)
'0b101'
>>> bin(b)
'0b10'
>>> 
>>> #........ OR ..........#
>>> a,b=2,3
>>> a|b
3
>>> 
>>> #......... Negotiation ..........#
>>> a=10
>>> ~a
-11
>>> #........ XOR .........#
>>> a=10
>>> b=1
>>> a^b
11
>>> 
>>> #........ Left shift .........#
>>> a=4
>>> a<<1
8
>>> a<<2
16
>>> 
>>> #........ Right shit ..........#
>>> a>>4
0
>>> a==4
True
>>> a=4
>>> a>>2
1
