#  how will you create a dictionary using tuples in python?

'''
=>  To convert a tuple to dictionary in Python, use the dict() method.
    The dict() function takes a tuple of tuples as an argument and
    returns the dictionary. Each tuple contains a key-value pair.

    example:-
    '''

tup = ((11, "eleven"), (21, "mike"), (19, "dustin"), (46, "caleb"))
print(tup)

dct = dict((y, x) for x, y in tup)
print(dct)
