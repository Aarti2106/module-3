#Write a Python script to concatenate following dictionaries to create a new one.

d1={"Name":"arti" , "Age":23}
d2={"City": "surendranagar", "Gender": "female"}
d3={"Mark":450}
d4 = {}
for d in (d1, d2, d3): d4.update(d)
print(d4)
