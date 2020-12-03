employee={"eid":1000,"desig":"develpoer","exp":1,"cmpny":"luminar"}

#print company name

print(employee["cmpny"])

#check if salary key is there
print("salary" in employee)

#add new key value pair salary:100

employee["salary"]=100
print(employee)

#update 400 more to salary

employee["salary"]+=400
print(employee)

for k,v in employee.items():
    print((k,v))










for k,v in employee.items():
    print((k,v))

