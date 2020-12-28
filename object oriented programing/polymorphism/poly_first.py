

class meth:
    def add(self):
        print("inside no arg method ")

    def add(self,num1):
        print("inside one arg method")

    def add(self,num1,num2):
        print("inside two arg method")

m=meth()
m.add(10,20)
m.add(10) #erorr ,recent function will only work