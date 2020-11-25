lowlimit=int(input("enter lower value"))
upperlimit=int(input("enter upper value"))


sumodd=0
sumeven=0
while(lowlimit<=upperlimit):
    if(lowlimit%2==0):
         sumeven=sumeven+lowlimit


    else:
        sumodd=sumodd+lowlimit
    lowlimit=lowlimit+1
print("ood sum =",sumodd)
print("even sum =",sumeven)

