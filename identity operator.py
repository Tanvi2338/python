#identity operators
a = None
print(a is None)
print(a is not None)

#bitwise operators
a = 5
b = 3

print(a & b)
print(a | b)
print(a ^ b)

#electic city bill calculator
units = int(input("Enter electricity units"))

rate = 6

bill = units * rate

print("Electricity Bill:", bill)

#Travel expense caluculator
travel = float(input("travel expenses:"))
food =float(input("Food expenses:"))
hotel= float(input("hotel expenses:"))

Total = travel + food + hotel
print("Total expenses:", Total)