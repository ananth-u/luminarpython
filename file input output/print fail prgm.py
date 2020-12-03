f1=open("names","r")
f2=open("passed","r")

stname=set()
stpass=set()
for lines in f1:
    stname.add(lines.rstrip("\n"))

for lines in f2:
    stpass.add(lines.rstrip("\n"))

print("fail",stname.difference(stpass))