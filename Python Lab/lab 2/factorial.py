#Write a python program finding the factorial of a given number using while loop

n=int(input("Enter a number:"))
fact=1;
i=1
while(n>=i):
    fact=fact*i;
    i=i+1
print("The factorial of",n, "is",fact)
