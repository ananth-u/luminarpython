lst=[1,2,3,4,5,6]

lst.sort()

low=0
upp=len(lst)-1

element=7
while(low<upp):
    total=lst[low]+lst[upp]
    if(element<total):
        upp=upp-1

    elif(element>total):
        low=low+1
    elif(element==total):
        print(lst[low],",",lst[upp])
        break