#exception

#error
#exception

#exception handling:

n1=int(input("enter value "))
n2=int(input("enter value "))
lst=[1,2,3]

try:
  res=n1/n2  #10/0 abnormal code thar disrupt our normal execution
  print(res)
  print(" i hav one database")  #not work when entering 10/0

except Exception as e:
    print(e.args)

try:
    print(lst[5])

except Exception as e:
    print(e.args)

print("ok")