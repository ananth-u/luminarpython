num=int(input("enter the number"))

min=int(input("enter the minnumber"))
max=int(input("enter the maxnumber"))

for i in range (min,(max+1)):
    if i**num in range (min, (max+1)):
        print(i, ",",i**num)