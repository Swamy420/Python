#list comprehension
'''a=['python','codegnan','course']
b=str(a)
print(b.upper())'''

'''for i in a:
    print(i.upper(),end=' ')

#syntax
#a[expr for var in collection/range]
b=[i.upper() for i in a]
print(b)'''


'''a=['vja','hyd','vzg']
b=[i.capitalize() for i in a]
print(b)'''

'''a=['PYTHON','JAVA','DSA']
b=[i.lower() for i in a]
print(b)'''

'''a=[2,3,4,5,6,8,12,13]
b=[i*i for i in a]
c=[i**2 for i in a]
d=[pow(i,2) for i in a]
print(b)
print(c)
print(d)'''


#if usage in list comprehension
'''a=[print(i) for i in range(16)]

b=[print(i) for i in range(21) if i%2==0]'''

'''b=[print(i*i) for i in range(21) if i%2==0]'''

'''fruits=['apple','banana','grapes','kiwi','berry','mango']
t=[i for i in fruits if i.count('a')>0]
print(t)'''

#no-elif usage in list comprehension
#if-else usage in list comprehension

'''a=[i*5 if i&1 else i**2 for i in range(31)]
print(a)'''

'''a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[a[i]+b[i] for i in range(len(a))]
print(c)'''

#ATM application
account=100000
card='c'
pwd=1234
c=input('Insert the card').lower()
if card==c:
    print('Welcome Gopi')
    np=int(input('Enter the password'))
    if pwd==np:
        print('1.Balance Enquiry\n2.Withdrawl')
        op=int(input())
        if op==1:
            print("Account balance:",account)
        elif op==2:
            ta=int(input('Enter the amount:'))
            account=account-ta
            print('Remaining balance:',account)
        else:
            print('Invalid option')
    else:
        print('Incorrect password')
else:
    print('Invalid card')
    
