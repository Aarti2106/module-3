#Write a Python program to convert a tuple to a string.

def convertTuple(tup):
    str = ''.join(tup)
    return str
 

tuple = ('p', 'y', 't', 'h', 'o','n')
str = convertTuple(tuple)
print(str)
