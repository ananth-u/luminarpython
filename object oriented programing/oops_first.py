


class person:
    def set_person(self,name,age):
        self.name=name
        self.age=age

    def print_person(self):
        print(self.name)
        print(self.age)


obj=person()
obj.set_person("ajay",23)
obj.print_person()

print("from outside class",obj.name)

obj.age=30 #updated the age
obj.print_person()