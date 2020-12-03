f=open("covid 19 .csv", "r")
dict={}
for lines in f:
    words=lines.rstrip("\n").split(",")
    stat=words[3].rstrip("***")
    confirmed_cases=int(words[8])
    if(stat not in dict):
        dict[stat]=confirmed_cases
    else:
        dict[stat]=confirmed_cases

for k,v in dict.items():
    print(k,"==>",v)

high=max(dict,key=dict.get)
print(high,dict[high])


#print(sorted(dict,key=dict.get,reverse=True))

#sorted data
#lst=[]
#for k,v in dict.items():
 #   lst.append((v,k))
#print(sorted(lst,reverse=True))