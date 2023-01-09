# Write a Python program to convert a list of tuples into a dictionary.

def Convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di
      
tups = [("akash", 10), ("gaurav", 12), ("anand", 14),
     ("suraj", 20), ("akhil", 25), ("ashish", 30)]
dictionary = {}
print (Convert(tups, dictionary))

print("----------------------------------")

tuples = [('Key 1', 1), ('Key 2', 2), ('Key 3', 3), ('Key 4', 4), ('Key 5', 5)]
result = dict(tuples)
print(result)

