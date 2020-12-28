class employee:
    def __init__(self,id,name,exp,desg,sal):
        self.id=id
        self.name=name
        self.exp=exp
        self.desg=desg
        self.sal=sal


    def __str__(self):
        return self.name+" "+self.id



f=open("employee","r")
lsr=[]
for lines in f:
    id,name,exp,desg,sal=lines.rstrip("\n").split(",")
    obj=employee(id,name,exp,desg,sal)
    lsr.append(obj)


for emp in lsr:
    print(emp)

#print all emp names in uppercase:
enames=list(map(lambda emp:emp.name.upper(),lsr))
print(enames)

#print emp details with desg=developer:
dev=list(filter(lambda ob:ob.desg=="developer",lsr))
for emp in dev:
    print(emp.name," ",emp.desg," ",emp.sal)

#print emp details with salary >200

#print emp details with salary>200
