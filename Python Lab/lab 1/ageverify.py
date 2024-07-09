#WAP to validate age using if...else statement.

age=int(input("Enter your age:"))

if (age<0) and (age<120):
    print("That's an invalid age")
elif (age<18):
    print("You are not eligible for Voting")
else:
    print("You are eligible for Voting")
    
