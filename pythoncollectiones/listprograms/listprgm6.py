lst=[-2,-1,0,2,3,4]#find least +ve missing integer

#print(1 in lst) #check for 1 in lst or not
cnt=1
for i in range(0,len(lst)):
    if cnt in lst:
        cnt+=1
    else:
        print(cnt,"is missing least +ve integer")
        break