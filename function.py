#functions

#a function is a block of organized,resuable code and that is used to perform a single or multiple tasks
#python gives inbuilt functions like print, you can make your own function also and these are called user defined functions
#function blocks begin with the keyword def.. followed by the function name and paranthesis

'''a=10
b=20
print('sum=',a+b)
print('dif=',a-b)
print('product=',a*b)
a=110
b=220
print('sum=',a+b)
print('dif=',a-b)
print('product=',a*b)
a=120
b=2550
print('sum=',a+b)
print('dif=',a-b)
print('product=',a*b)
a=1120
b=210
print('sum=',a+b)
print('dif=',a-b)
print('product=',a*b)'''


'''def calculate(a,b):
    print('sum=',a+b)
    print('dif=',a-b)
    print('product=',a*b)
calculate(10,20)
calculate(20,30)
calculate(30,40)'''

'''def calculate(a,b):
    print('integer division=',a//b)
    print('power=',a**b)
    print('modulus=',a%b)
calculate(10,20)
calculate(20,30)
calculate(30,40)'''


'''while True:
    def add():
        a=int(input())
        b=int(input())
        print(a+b)
    add()'''

'''def add():
    a=int(input())
    b=int(input())
    print(a+b)
    add()
add()'''

'''def fullname():
    fname=input()
    lname=input()
    print((fname+' '+lname).title())
fullname()'''


#difference between print and return
#print just shows the human user input in a console
#return will terminate the function and gives back a value from the function

'''def add():
    a=int(input())
    b=int(input())
    return a+b
    add()
res=add()
print(res)'''

'''def fun(a,b):
    op=int(input())
    if op==1:
        return a+b
    elif op==2:
        return a-b
    elif op==3:
        return a*b
    else:
        return -1
a=int(input())
b=int(input())
res=fun(a,b)
print(res)'''

#split bill
'''def fun(n,amt):
    return amt/n
n=int(input())
amt=int(input())
res=fun(n,amt)
print('per head=',res)'''

'''def fun(n,amt):
    return amt/n
n=int(input())
amt=int(input())
res=fun(n,amt)
print(f'per head={res}')'''

'''def fun(n,amt):
    return amt/n
n=int(input())
amt=int(input())
res=fun(n,amt)
print('per head={}'.format(res))'''


a=[7,18,12,15,2,4,17]
for i in range(0,len(a),2):
    print(a[i])
for i in range(0,len(a)):
    if a[i]%2==0:
        print(a[i])
for i in range(0,len(a),2):
    if a[i]&1:
        print(a[i])
