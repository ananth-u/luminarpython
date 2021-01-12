#hoghest salary
from functools import*
class employee:
    def __init__(self,id,name,desg,sal,exp):
        self.id=id
        self.name=name
        self.desg=desg
        self.sal=sal
        self.exp=exp


    def __str__(self):
        return self.name



f=open("employee","r")
lsr=[]
for lines in f:
    id,name,desg,sal,exp=lines.rstrip("\n").split(",")
    obj=employee(id,name,desg,sal,exp)
    lsr.append(obj)


for emp in lsr:
    print(emp)

high=reduce(lambda s1,s2:s1 if s1>s2 else s2,list(map(lambda emp:emp.sal,lsr)))
print(high,",",emp.name,",",emp.desg,",",emp.exp)

hihsal=list(filter(lambda emp:emp.sal==high,lsr))
for emp in hihsal:
    print(emp.name)



