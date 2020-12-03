#to store data
#read data from file named text and dispay content here

#operationes:
#read r
#write w
#append a

#step1
#create file reference

#f=open("path","mode of operation")

f=open("text","r")

#for line in f:
    #print(line)

#lst=[]
#for line in f:
    #lst.append(line.rstrip("\n"))
#print(lst)

st=set()
for line in f:
    st.add(line.rstrip("\n"))
print(st)


