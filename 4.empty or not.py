#Write a Python program to check a list is empty or not.

l=[60,50,40,0,30,20,10]
l1=[]
if len(l)==0:
    print("list is empty ")
else:
    print("list is not empty ")
print("-------------------------------")

def get(lis1):
    if len(lis1) == 0:
        return 0
    else:
        return 1
 
lis1 = []
if get(lis1):
    print("The list is not empty")
else:
    print("Empty List")
