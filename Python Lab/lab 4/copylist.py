#Python | Cloning or Copying a list into another list

a=[1,2,3,4,5]
print("Elements of first list are", a)

b=[]
print("Elements of second list are", b)

c=[]

b=a
print("Elements in second list after copying from fist list:",b)

c=a.copy()
print("Copying elements from one list into another using copy():", c)

