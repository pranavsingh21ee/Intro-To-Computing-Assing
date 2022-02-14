#1
str=input("Enter string : ")
c=dict()
words=str.split()
for word in words:
        if word in c:
            c[word]+= 1
        else:
            c[word]= 1
print(c)







#2
year=int(input("Input a year : "))

if (year%400==0):
    leap_year=True
elif (year%100==0):
    leap_year=False
elif (year%4==0):
    leap_year=True
else:
    leap_year=False

month=int(input("Input a month [1-12] : "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length=31
elif month==2:
    if leap_year:
        month_length=29
    else:
        month_length=28
else:
    month_length=30

day=int(input("Input a day [1-31]: "))

if day<month_length:










#3
def square_of_list(list):
    result=[(num, num**2) for num in list]
    return result
list=[3,9,10]
print(square_of_list(list))









#4
Grade = input("Enter Grade between 4-10: ")
s =  float(Grade)
x = 'Error'
y = 'no'
if s > 10:
	print('Error')
elif s <= 10 and s>9:
	x = 'A+'
	y ='Outstanding'
elif s <=9 and s>8:
	x='A'
	y='Excellent'
elif s <=8 and s>7:
	x='B+'
	y='Very Good'
elif s <= 7 and s>6:
	x='B'
	y='Good'
elif s <= 6 and s>5:
	x ='C+'
	y='Average'
elif s <= 5 and s>4:
	x ='C'
	y='Below Average'
elif s == 4:
	x ='D'
	y='Poor'
else:
	x ="Out of Range"
print ("Your Grade is",x,"and",y,"Performance")










#5
str1="ABCDEFGHIJK"
l=len(str1)
for i in range(l):
    for j in range(i):
        print(" ",end="")
    for j in range(l-i):
        print(str1[j],end=" ")
    l=l-1
    print()





#6a
dic = { }
while True :
    ask= input("Do you want to enter details? Y or N : ")
    if ask=="N" or ask=="n":
        break
    else:
        sid=int(input("Enter SID : "))
        name=input("Enter Student Name : ")
        dic[sid]=name

print(dic)










#6b
dic = { }
while True :
    ask= input("Do you want to enter details? Y or N : ")
    if ask=="N" or ask=="n":
        break
    else:
        sid=int(input("Enter SID : "))
        name=input("Enter Student Name : ")
        dic[sid]=name

print(sorted(dic.items()))








#6c
dic = { }
while True :
    ask= input("Do you want to enter details? Y or N : ")
    if ask=="N" or ask=="n":
        break
    else:
        sid=int(input("Enter SID : "))
        name=input("Enter Student Name : ")
        dic[sid]=name
di=dic.items()
si=sorted(di)
print(si)









#6d
dic = { }
while True :
    ask= input("Do you want to enter details? Y or N : ")
    if ask=="N" or ask=="n":
        break
    else:
        sid=int(input("Enter SID : "))
        name=input("Enter Student Name : ")
        dic[sid]=name
search=int(input("Enter SID To Search : "))
print("Name of the student : ",dic[search])










#7
a=int(input("Enter the terms:"))
f=0
s=1
if a<=0:
    print("The requested series is",f)
else:
    print(f,s,end=" ")
    for x in range(2,a):
        next=f+s                           
        print(next,end=" ")
        f=s
        s=next









#8a
Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}
T1= Set1|Set2
T2=Set1&Set2
print(T1-T2)









#8b
Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}
print(Set1&Set2&Set3)









#8c
Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}
T1=Set1&Set2
T2=Set2&Set3
T3=Set1&Set3
U=T1|T2|T3
print(U)







#8d
Set1= {1, 2, 3, 4, 5}
#Creating a new set of range 1 to 10
Int={1,2,3,4,5,6,7,8,9,10}
#Print the new set
print(Int-Set1)








#8e
Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}
#Creting a new set of integers of range of 1 to 10
Int={1,2,3,4,5,6,7,8,9,10}
#Creating a union of given sets
U1=Set1|Set2|Set3
#printing required set using U1 and Int
print(Int-U1)
