lst=[1,2,3,4] #7 (3,4)git push

num=int(input("enter value"))

for i in lst:
    for j in lst:
         if(i!=j):
             if((i+j==num)):
                 print("(",i,j,")")

