#if condition using comparision operators <,>,<=,>=,!=,==

'''a=int(input())
b=int(input())
if a<b:
    print("Smaller")'''


'''a=int(input())
b=int(input())
if a>b:
    print("Greater")'''


'''a=int(input())
b=int(input())
if a<=b:
    print("Less than or equal")'''


'''a=int(input())
b=int(input())
if a>=b:
    print("Greater than or equal")'''


'''a=int(input())
b=int(input())
if a!=b:
    print("Not equal")'''


'''a=int(input())
b=int(input())
if a==b:
    print("Equal")'''


'''a=input()
b=input()
if a==b:
    print("Equal")'''

#if condition by using logical operators 
# and, or, not


'''a=int(input())
b=int(input())
if a<b and b>a:
    print('true')'''


'''a=int(input())
b=int(input())
if a<=b or b<=a:
    print("true")'''


'''a=int(input())
b=int(input())
if a!=b or a==b:
    print("True")'''


'''a=int(input())
b=int(input())
if not a<b and b>a:
    print("false")'''

'''a=int(input())
b=int(input())
if not a<b or b>a:
    print("true")'''

#if condition using identify operators
#is,is not

'''a=int(input())
if type(a) is int:
    print("true")'''

'''a=float(input())
if type(a) is not int:
    print("true")'''

'''a=input()
if type(a) is not int:
    print("true")'''

#if condition using membership operators
#in, not in
'''a=[10,20,30,40,50]
if 10 in a:
    print('true')'''

'''a=[10,20,30,40,50]
if 100 not in a:
    print('true')'''

#if else conditions by using comparision
'''a=2
b=4
if a<b:
    print('true')
else:
    print('false')'''

'''a=2
b=4
if a>b:
    print('true')
else:
    print('false')'''

'''a=int(input())
b=int(input())
if a<=b:
    print('true')
else:
    print('false')'''

'''a=int(input())
b=int(input())
if a>=b:
    print('true')
else:
    print('false')'''

'''a=int(input())
b=int(input())
if a!=b:
    print('true')
else:
    print('false')'''

'''a=int(input())
b=int(input())
if a==b:
    print('true')
else:
    print('false')'''

#if else condition using logical operators and ,or,not

'''a=int(input())
b=int(input())
if a<b and b>a:
    print('true')
else:
    print('false')'''

'''a=int(input())
b=int(input())
if a<b or b<a:
    print('true')
else:
    print('false')'''

'''a=int(input())
b=int(input())
if not a<=b:
    print('true')
else:
    print('false')'''

#if condition using identify operators
#is,is not

'''a=int(input())
if type(a) is int:
    print("true")
else:
    print('false')'''

'''a=float(input())
if type(a) is not int:
    print("true")
else:
    print('false')'''
#if condition using membership operators
#in, not in
'''a=[10,20,30,40,50]
if 10 in a:
    print('true')
else:
    print('false')'''

'''a=[10,20,30,40,50]
if 100 not in a:
    print('true')
else:
    print('false')'''



#if-elif-else
#comparision operators
'''a=int(input())
b=int(input())
if a<b:
    print('smaller')
elif a>b:
    print('greater')
else:
    print('equal')'''

#logical operators
'''a=int(input())
b=int(input())
c=int(input())
if a<b and a<c:
    print('smaller')
elif a>b or a>c:
    print('greater')
else:
    print('...')'''
#identify
'''a=int(input())
if type(a) is int:
    print('int')
elif type(a) is float:
    print('float')
else:
    print('string')'''
#membership

'''a=[10,20,30,40,50]
if 10 in a:
    print('true')
elif 100 not in a:
    print('false')
else:
    print('hlo')'''

#multiple-if
'''a=10
b=20
if a<b:
    print('a is smaller')
if b>a:
    print('b is bigger')
if a!=b:
    print('not equal')'''
#logical operators
'''a=10
b=23
c=11
if a<b and a<c:
    print('a is smaller')
if b>a or b>c:
    print('b is greater than anyone')
if not c>b:
    print('middle')'''
#identify
'''a=int(input())
b=input()
c=float(input())
if type(a) is int:
    print('int')
if type(b) is not float:
    print('string')
if type(c) is float:
    print('flaot')'''

#membership
'''a=[10,20,30,40]
if 10 in a:
    print('10 is in a')
if 100 not in a:
    print('100 not in a')'''


#nested if
'''a=8
b=5
if a<b:
    print("true")
    if b<a:
        print("true")'''

'''a=8
b=5
if a<b:
    print("true")
    if b<a:
        print("true")
else:
    print("false")'''
'''a=10
b=25
if a<b:
    print("true")
    if b<a:
        print("false")
    else:
        print("true")'''
    
#task
#voting
'''age=int(input())
if age<18:
    print('Not eligible for vote')
else:
    print('Eligible for vote')'''

#even or odd
'''n=int(input())
if n==0:
    print('neither odd nor even')
elif n&1:
    print('odd')
else:
    print('even')'''

#leap year
'''yr=int(input())
if yr%4==0:
    print('leap year')
else:
    print('not a leap year')'''
    

#guest code
'''name=input().lower()
if name=='pooja':
    print('welcome',name)
else:
    print('welcome guest')'''

#vowels
'''le=['a','e','i','o','u']
l=input().lower()
if l in le:
    print('It is vowel')
else:
    print('It is consonant')'''


#guest
'''n1=input().lower()
n2=input().lower()
n3=input().lower()
n4=input().lower()
n5=input().lower()
a=[n1,n2,n3,n4,n5]
if 'pooja' in a:
    print('welcome pooja')
else:
    print('welcome guest')'''

#social media login
'''username=input().lower()
pwd=int(input())
if username=='pooja':
    if pwd==123:
        print('Login successful')
    else:
        print('Wrong password')
else:
    print('Invalid credentials')'''

'''username=input().lower()
pwd=int(input())
if username=='pooja' and pwd==123:
    print('Login successful')
else:
    print('Invalid credentials')'''

'''username=input().lower()
pwd=input()
if username=='pooja' and pwd=='ex@123':
    print('Login successful')
else:
    print('Invalid credentials')'''


#bakery
'''cake=input().lower()
if cake=='redvelvet':
    print(1200)
elif cake=='chocoalmond':
    print(1000)
elif cake=='butterscotch':
    print(800)
elif cake=='chocolate':
    print(600)
else:
    print('cake is not available')'''

#pizza
'''price=int(input())
if price==800:
    print('Crispy chicken pizza')
elif price==600:
    print('BBQ pizza')
elif price==400:
    print('panner pizza')
elif price==200:
    print('corn pizza')
else:
    print('coke')'''


#mutiple if
'''age=int(input())
marks=int(input())
attendence=int(input())
if age>=18:
    print('They are eligible for vote')
if marks>=80:
    print('He got good marks')
if attendence>=90:
    print('Eligible for scholarship')'''
