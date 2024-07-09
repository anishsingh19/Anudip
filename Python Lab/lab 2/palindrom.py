#WAP to check whether the number is palindrom or not

num=int(input("Enter a number:"))
rev=0
temp = num
while(temp>0):
    rem=temp%10
    rev=rev*10+rem
    temp//=10
print("The reverse of the number is", rev)

if num==rev:
    print("The entered number is a palindrom")
else:
    print("The entered number is not a palindrom")
