#loops()
# for,while,range,break,continue,pass

#for loop()
'''a=[10,20,30,40,50]
for i in a:
    print(i)'''

'''a=[10,20,30,40,50]
for i in a:
    print(i,end=' ')'''

'''a=[10,20,30,40,50]
for i in a:
    print(a)'''

'''a=[10,20,30,40,50]
for i in a:
    print(i)
    print(type(i))
    print(type(a))'''

'''a=[10,20,30,40,50]
for i in a:
    print(i)
print(type(a))'''

'''a=(4,5,6,7,8)
for i in a:
    print(i)'''

'''a=(4,5,6,7,8)
for i in a:
    print(i)
    print(type(i))
    print(type(a))'''

'''a=(4,5,6,7,8)
for i in a:
    print(i)
    print(type(i))
print(type(a))'''

'''a={1,2,3,4,5}
for i in a:
    print(i)
    print(type(i))
    print(type(a)) '''

'''a={1,2,3,4,5}
for i in a:
    print(i)
    print(type(i))
print(type(a))'''

'''a={'name':'Gopi','year':2026,'month':6}
for i in a:
    print(i)
    print(type(i))
    print(type(a))
for i in a.keys():
    print(i)
for i in a.values():
    print(i)
    print(type(i))
    print(type(a))
for i in a.items():
    print(i)
    print(type(a))
    print(type(i))'''

'''a=[1,2.2,'hlo',4+9j,True,False]
for i in a:
    print(i)
    print(type(i))
print(type(a))'''

'''s='codegnan'
print(s)
print(type(s))
for i in s:
    print(i)
    print(type(i))'''

'''a=['apple','mango','grapes']
for i in a:
    print(i,end=' ')'''

'''a=['codegnan','python','course']
b=[]
for i in a:
   b.append(i.upper())
print(b)'''

'''a=['codegnan','python','course']
b=str(a)
print(b.upper())'''



#while()
'''a=10
while a>1:
    print(a)'''

'''a=10
while a>=1:
    print(a)
    a-=1'''

'''a=10
while a>1:
    a-=1
    print(a)'''

'''a=20
while a>6:
    print(a)
    a+=1'''

'''a=20
while a>0:
    a-=1
print(a)'''

'''while True:
    
    age=int(input("enter the age:"))
    if age>=18:
        print("eligable")
    else:
        print("not eligable")'''

#Range
#Range function returns a sequence of numbers, starting from 0 by default and increments by one by one and stops before a specified number
#range()
#start-stop-step
'''for i in range(10):
    print(i)'''

'''for i in range(1,20):
    print(i)'''

'''for i in range(0,30,3):
    print(i,end=' ')'''

'''for i in range(2,20,2):
    print(i,end=' ')'''

'''for i in range(5,50,5):
    print(i,end=' ')'''

'''m=int(input())
if m in range(91,101):
    print("Grade-A")
elif m in range(81,91):
    print('Grade-B')
elif m in range(71,81):
    print('Grade-C')
elif m in range(61,71):
    print('Grade-D')
else:
    print('Fail')'''

#the break statement is used to terminate the entire loop
#the continue statement is skip the current iteration and rest of the code be continue
#the pass statement is a null statement it does nothing but syntatically we need

#break
'''a=10
while a>1:
    print(a)
    a=a-1
    if a==5:
        break'''

'''a=20
while a>5:
    print(a)
    a-=1
    if a==10:
        break'''

'''for i in range(10,0,-1):
    if i==7:
        break
    print(i)'''

'''a='python'
for i in a:
    if i=='h':
        break
    print(i)'''

#continue
'''a='python'
c=0
for i in a:
    if c==0 and i!='h':
        continue
    else:
        c=1
        print(i)'''

'''a=30
while a>10:
    a-=1
    if a==19:
        continue
    print(a)'''

'''a=11
while a>4:
    if a==7:
        continue
    a-=1
    print(a)'''

'''for i in range(20):
    if i&1:
        continue
    print(i)'''

#pass
'''a=15
while a>10:
    print(a)
    a-=1
    if a==14:
        pass'''

'''for i in range(20):
    if i==15:
        pass
    print(i)'''

#task
'''for i in range(1,30):
    if i==14:
        break
    if i==7:
        continue
    print(i)'''

#student attendence report
'''n=int(input())
p=0
a=0
t=n
while n:
    stu=input().lower()
    if stu=='present':
        p+=1
    else:
        a+=1
    n-=1
print("Total number of students:",t)
print('Present:',p)
print('Absent:',a)'''


#right angle triangle
'''n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print('*',end=' ')
    print(end='\n')'''

#reverse right angle triangle
'''n=int(input())
for i in range(n,0,-1):
    for j in range(i):
        print('*',end=' ')
    print(end='\n')'''

#square
'''n=int(input())
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print(end='\n')'''
#pyramid
'''n=int(input())
for i in range(0,n,1):
    for j in range(n-i):
        print(' ',end='')
    for k in range(i):
        print('* ',end='')
    print('\n')'''
