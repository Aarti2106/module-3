#Write a Python program to remove duplicates from a list.

duplicate=[2,3,4,2,5,6,4,7,9,5,6]
print(list(set(duplicate)))

print("**************************")

n=int(input("Enter the  total no of element you want inside your list:"))
l=[]
for i in range (n):
      ele=input("Enter the element")
      l.append(ele)
print("my list",l)
duplicate=(set(l))
print(duplicate)
