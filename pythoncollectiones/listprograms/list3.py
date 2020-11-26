#store odd and even in separate lst

limit=int(input("enter limit:"))

lst1=[]
lst2=[]

for i in range(1,limit+1):
    if(i%2==0):
        lst1.append(i)
    else:
        lst2.append(i)

print(lst1)
print(lst2)