#Write a Python program to remove an empty tuple(s) from a list of tuples.

def Remove(tuples):
    tuples = [t for t in tuples if t]
    return tuples
 

tuples = [(), ('aarti','12','6'), (), ('laxmi', 'sita'),
          ('krishna', 'vandana', '45'), ('',''),()]
print(Remove(tuples))

