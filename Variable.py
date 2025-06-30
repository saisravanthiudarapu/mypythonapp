'''
#a=10
#b,c=20,30
#d=e=f=40
#print(a)
#print(c)
#print(f)
a=int(input("Enter a value:"))
b=int(input("enter b value:"))
print(a)
print(a+b)
d,e=map(int,input("Enter d,e:").split())#split the values,map mean mapping the values to variables
print(e)
age=18
if age>18:
    print("Eligible")
elif age==18:
    print("Welcome new voter")
else:
    print("not eligible")
print("if condition execution")

c = int(input("Enter a value"))
if c%10==7 or c/10 ==7 :
    print("Yes")
else:
    print("No");
print("execution completed")
for i in range(10):
    print(i,end=",")
for i in range(10,100):
    if i%10==7 or i//10==7:
        print(i,end=" ")
l1=[10,20,True]
print(sum(l1))
n=10
l1=[]
for i in range(n):
    if i%2==0 :
        l1.append(i)
print(l1)
n=8
l2=[x for x in range(n) if x%2==1]
print(l2)
'''