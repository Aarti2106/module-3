#Write a Python function that takes two lists and returns true if they have
#at least one common member.


def list(l1,l2):
    
    for i in l1:
        if i in l2:
            return("True")
            break
                
    else:
        return("Flase")
        
print(list([1,2,3,4],[9,5,6,8]))
