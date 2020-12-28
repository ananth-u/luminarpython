employee=["ajay","vijay","anil","daniel","tom","joy"]

#convert all employees name to upper case
upp=list(map(lambda name:name.upper(),employee))
print(upp)

#print names of employees starting with a
f=list(filter (lambda name:name[0]=='a',employee))
print(f)