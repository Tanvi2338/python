#list in python
#List is an ordered and changeable collectionthat can store multiple values.It defines in square braces.
marks =[80,90,75,85]

print(marks)

#accessing elements in a list
marks =[80,90,75,85]

print(marks[0])
print(marks[1])
print(marks[2])

#changing element in a list
marks =[80,90,75,85]

marks[1] = 95

print(marks) 

#add element in a list
marks =[80,90,75]

marks.append(85)

print(marks)

#Remove element from list
marks=[80,90,75]

marks.remove
print(marks)

#Insert of element
numbers=[10,20,30]
numbers.insert(1,15)
print(numbers)

#Extend
a=[1,2,3]
b=[4,5,6,]

a.extend(b)

print(a)

#Clear
numbers =[10,20,30,]

numbers.clear()

print(numbers)

#Index
numbers = [20,30,40,50]

print(numbers.index(30))

#count
numbers =[10,20,20,30,20]

print(numbers.count(20))

#Sort
numbers =[40,10,20,30]

numbers.sort()

print(numbers)

numbers.sort(reverse=True)

print(numbers)  

#Copy

a=[1,2,3,]

b= a.copy()

print(b)

numbers =[10,20,30,40,50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])
print(numbers[-1::])
print(numbers[::-2])
print(numbers[-2::])


