#How Do You Traverse Through A Dictionary Object In Python?
'''
Dictionaries are a valuable and frequently used data structure in Python.
This article tells us how to traverse through a dictionary while performing
operations on its key-value pairs
'''

dictionary = { 
   'Novel': 'Pride and Prejudice', 
   'year': '1813', 
   'author': 'Jane Austen', 
   'character': 'Elizabeth Bennet' 
}

for keys, values in dictionary.items(): 
   print(keys ,values)
