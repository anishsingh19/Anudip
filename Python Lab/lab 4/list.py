#Python program to interchange first and last elements in a list

list=[1,2,3,4,5]
print(list)

print("The first element of the list is",list[0])
print("The last element of the list is", list[-1])

temp=list[0]
list[0]=list[-1]
list[-1]=temp

print("List after interchanging first and last elements", list)
