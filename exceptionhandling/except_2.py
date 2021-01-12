n1=int(input("enter value "))
n2=int(input("enter value "))
lst=[1,2,3]

try:
  res=n1/n2
  print(res)

except:
    n2=int(input("enter newvalue"))
    try:
        res=n1/n2
        print(res)

    except:
        n2 = int(input("enter newvalue"))
        print(res)



finally:
    print("ok")



