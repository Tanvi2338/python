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


#tuples in python
#tuple is a collection of multiple values that is ordered and cannot be changed after creation
student = ("Manu", 98, "python")

print(student[0])

#access values in tuple
student = ("Manu",21,85.5)

print(student[0])
print(student[1])

#tuples are immutable,meaning they cannot be changed after they are created.they are defined using parenthasis
numbers =(10,20,20,30,20)

print(numbers.count(20))

 #index

numbers = (10,20,30,40)

print(numbers.index(30))

numbers =(10,20,30,40)


print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#sets in python
#set is a collection of unique values that is unordered and mutable
numbers ={10,20,30,20,10}

print(numbers)

#add values to a set
subjects ={"python","java"}

subjects.add("SQL")

print(subjects)

#remove values from a set
subjects.remove("java")

print(subjects)

#sets do not allow the duplicate values
numbers= {1,2,2,3,3,4}

print(numbers)

#dictionaries in python
#dictionary is a collection of key-value pairs that is ordered and mutable
student={
    "name": "Manu",
    "age": "20",
    "course": "python"
}

print(student)

#access elements in dictionary
print(student["name"])
print(student["age"])
print(student["course"])

#add new data to a dictionary
student["city"] = "Vijayawada"

print(student)

## Dictionaries are unordered collections
student={
    "name": "Manu",
    "age": 20,
    "course":"python"
    }
print(student.keys())
#keys() returns all the keys in the dictionary

print(student.items())
#items() returns all key-value pairs

print(student.get("name"))
#get()returns the value of specified key

print(student. values())
#values() returns all the values in the dictionary

student.update({"age":22})
#update()updates the value of specified key

print(student)

student.pop("age")
#pop()removes the specified key and its value

print(student)
#popitem() removes the last inserted key-value pair
student={
    "name": "Manu",
    "age": 20,
    "copurse":python
}

student.popitem()

print(student)

student={
    "name":"Manu"
}

student.setdefault("age",21)

print(student)