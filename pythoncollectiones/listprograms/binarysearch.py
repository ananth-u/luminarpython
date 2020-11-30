lst=[5,7,5,1,2,3,4]

#step1 we hav to sort the array


lst.sort()

#step2

low=0
upp=len(lst)-1
flag=0
element=int(input("enetr the element to search"))
while(low<=upp):
   mid=(low+upp)//2

   if(element>lst[mid]):
       low=mid+1
   elif(element<lst[mid]):
       upp=mid-1

   elif element==lst[mid]:
       flag=flag+1
       break

if flag==0:
    print("emlement not found")

else:
    print("element found")