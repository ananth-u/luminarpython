#to perform a specific task
#input()
#print()



#def mul(num1,num2):
    #res=num1*num2
    #print (res)


#def div(num1,num2):
    #res=num1/num2
    #print(res)


#mul(10,20)
#div(20,10)


#function wit arguments and return value:


#def add(num1,num2):
    #res=num1+num2
    #return res

#data=add(10,20)
#print(data)


def add(num1,num2):
    res=num1+num2
    return res

def evencheck(num1):
    if(num1%2==0):
        return "even"
    else:
        return "odd"

data=add(10,20)
print(evencheck(data))