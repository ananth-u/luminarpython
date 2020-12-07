f=open("employee","r")
employee={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    employee["id"]=data[0]
    employee["name"]=data[1]
    employee["desg"]=data[2]
    employee["exp"]=data[3]
    employee["salary"]=data[4]
print(employee)

de
