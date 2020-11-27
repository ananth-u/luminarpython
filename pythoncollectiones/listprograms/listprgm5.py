lst=[5,4,3,2] #out=[9,10,11,12]
total=sum(lst)
out=[]

for num in lst:
    out.append((total-num))
print(out)

