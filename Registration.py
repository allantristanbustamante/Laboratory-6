membership = input("Are you a member? (YES)or(NO):")
age = int(input("Enter your age:"))

RegFee = 0

if age>=0 and age<=10:
    if membership == "YES":
        RegFee = 450
    elif membership == "NO":
        RegFee = 650
    else:
        print("Please choose between YES or NO")
elif age>=18 and age<=65:
    if membership =="YES":
        RegFee = 550
    elif membership == "NO":
        RegFee = 750
    else: 
        print("Please choose between YES or NO")
elif age>=65 and age<=110:
    if membership == "YES":
        RegFee = 400
    elif membership == "NO":
        RegFee = 600
    else:
        print ("Please choose between YES or NO")
        
else:
    print("Invalid Age. Please try again.")
    
if RegFee > 0:
    print(f"Your registration fee is: {RegFee} pesos.")
    