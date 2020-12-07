#variable length argument method  :we can passs any number of arguments and it is read as tuple

#def add(*num):
 #   sum=0
  #  for n in num:
   #     sum=sum+n

#    print(sum)

#add(10,20,30,40,50)



def printdata(**kwargs):
    for k,v in kwargs.items():
        print(k ,v)
    print(kwargs)

printdata(birthplace="kochi",desg="devep")