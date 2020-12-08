#students={

#    100:{"roll":100,"name":"test1","course":"bca"},
#    101: {"roll": 101, "name": "test2", "course": "mca"},
#    102: {"roll": 102, "name": "test3", "course": "bcom"},
#}

f=open("students details","r")
students={}
for lines in f:
    rol,name,course=lines.rstrip("\n").split(",")
    if rol not in students:
        students[rol]={"rol":rol,"name":name,"course":course}
for k,v in students.items():
    print(k,v)
def print_data(**kwargs):
    print(kwargs)
    rol=kwargs["id"]


    if rol in students:

        print(students[rol]["name"])
        if "property" in kwargs:
           prop=kwargs["property"]
           if prop in students[rol]:
               print(students[rol][prop])

           else:
               print('invalid property')
    else:
        print("invalid roll number")




print_data(id="103",property="course")