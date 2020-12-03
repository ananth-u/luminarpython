f=open("data","r")

dict={}

for lines in f:
    words=lines.rstrip("\n").split(" ")

    for word in words:
        if (word  not in dict):
            dict[word]=1
        else:
            dict[word]+=1

print(dict)

#method 1:
#flag=0
#for k ,v in dict.items():
 #   if (v>=flag):
  #      flag=v
#for k,v in dict.items():
 #   if(v==flag):
  #      print((k,v))

#method 2
#high=max(dict,key=dict.get)
#print(high)

#method 3
lst=[]
for v in dict.values():
    lst.append(v)
high=max(lst)

for k,v in dict.items():
    if (v==high):
        print(k,v)