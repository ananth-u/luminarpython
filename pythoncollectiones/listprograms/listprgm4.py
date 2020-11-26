

lst=[9,8,7,6,4,3,2]
new=[]

for num in lst:
    if(num>5):
        new.append(num+1)
    elif(num<5):
        new.append(num-1)
    elif(num==5):
        new.append(num)
print(new)        