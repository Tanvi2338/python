#logical operaters
age=25
citizen = True

print(age >= 18 and citizen == True)

has_card=False
has_cash=True
print(has_card or has_cash) 



is_logged_in = True
print(not is_logged_in)



#atm eligibilty checker
balance = 10000
withdraw=5000

print(withdraw>0 and withdraw<=balance)



#student scholarship eligibility checker
marks=float(input("Enter your marks: "))
attendance=float(input("Enter your attendance: "))

eligible_for_scholarship = marks >= 75 and attendance >= 80

print(" scholarship eligible:", eligible_for_scholarship)
