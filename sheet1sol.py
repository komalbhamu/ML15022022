#Q2

print(5**9)
print(3//2)
print(7//3)
print(7/3)
print(6==6)
a=20; a+=30; a%=3;
print(a)
print(True*False)
print(True&False)
print(True and False)
print(((6>3) and (7<4) or (18==3)) and (9>3))
print(True is False)
print(((True==False) or (False>True)) and (False<=True))

#Q3

s1='Nice to have it'
s2='here'
print(s1,s2,sep=' ')

#Q4

a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2])

#Q5

a.append(s2)
a.insert(0,s1)
print(a)

#Q6

numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 
742, 717, 958,743, 527]
for i in numbers :
    if i==237 :
        break ;
    elif i%2==0 :
        print(i)

#Q7

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1-color_list_2)

#Q8

import string
def ispangram(str):
    alpha = "qwertyuiopasdfghjklzxcvbnm"
    for char in alpha :
        if char not in str.lower():
            return False
        return True
string = input("Enter the string \n")
if(ispangram(string)== True):
    print("Yes")
else :
    print("NO")

#Q9

n=int(input('n :'))
n1=int("%s"%n)
n2=int("%s%s"%(n,n))
n3=int("%s%s%s"%(n,n,n))
total=n1+n2+n3
print(total)

#Q10

l1=[]
l2=[]
x=int(input("Enter the no of elements\n"))
y=int(input("Enter the no of elements\n"))
print("Enter the first list elements\n")
for i in range (0,x):
   e = int(input())
   l1.append(e)
print("Enter the second list elements\n")

for i in range (0,y):
   t = int(input())
   l2.append(t)

print(l1)
print(l2)


#Q11

z=input().split(',')
print(z)
z.sort()
print(z)

#Q12

d={'student':['rahul','kishore','vidhya','raakhi'],'Marks':[57,87,67,79]}
t=max(d['Marks'])
ini=d['Marks'].index(t) ## ini integer value for index
m=d['student']
print(m[ini])

#Q13

l='hello woeld! 123'
w=[]
for i in l:
    w.append(i)
y=['0','1','2','3','4','5','6','7','8','9']
countn=0
counta=0
for j in w:
    if j.isalpha():
        counta=counta+1
    elif j in y:
        countn=countn+1
    else:
        print('')

print('Alphabets :',counta)
print('Digits :',countn)



       

























