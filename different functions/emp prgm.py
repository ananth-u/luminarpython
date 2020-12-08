#create a function print_employee_data()
#if we pass id pass argument thatfunction will print emp name
#if we pass id and property=desg it will print emp name and desgination



f=open("employee","r")


employee={}
for lines in f:

    id,name,desg,exp,salary=lines.rstrip("\n").split(",")
    employee[id]={"id":id,"name":name,"desg":desg,"experience":exp,"salary":salary}
print(employee)

def print_employeedata(**kwargs):
        print(kwargs)
        id=kwargs["id"]
        if id in employee:
           print(employee[id]["name"])
           prop=kwargs["property"]
           if prop in employee[id]:
               print(employee[id][prop])
           else:
               print("invalid property")
        else:
           print("invalid id")

print_employeedata(id="1000",property="desg")
