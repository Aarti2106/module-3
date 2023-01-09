#Write a Python function that takes a list and returns a new list with unique
#elements of the first list.

def unique(list1):
    l2=[]
    for i in list1:
        if i not in l2:
            l2.append(i)
    return(l2)
print(unique([1,2,3,4,5,2,6,4,3,7,8,9]))
