#for loop
#used to repeat code or iterate through a sequence

for i in range (1,6):
    print(i)
#use whilw when repetition depends on a condition
#looping through number 1 to 5 using while loop
i=1

while i<5:
    print(i)
    i=i+1

#print 1 to 10
for i in range (1,11):
    print(i)

#print 10 to 1
for i in range(10,0,-1):
    print(i)

#print even number from 2 to 50
for i in range (2,51,2):
    print(i)

 #print odd number from 1 to 51
for i in range (1,51,2):
    print(i)

#print multiple of 5 from 5 to 50
for i in range(5,51,5):
    print(i)

#multiplication
number=int(input("enter number:"))
for i in range(1,11):
    print(number,"*",i,"=",number*i)
    

#sum of number from 1 to n
n =int(input("enter n:"))
total=0
for i in range (1,n+1):
    total =total+i
    print("sum:",total)

#factorial of numbers
n =int(input("enter n:"))
factorial =1
for i in range(1,n+1):
    factorial = factorial*i
    print("factorial:",factorial)

#sum of even number from 2 to n
n =int(input("enter n:"))
total=0
for i in range(2,n+1,2):
    total=total+i
    print("sum:",total)                