#reduce

from functools import*

lst=[10,11,12,13,14,15,2,16,17,18]

#sum:
sum=reduce(lambda no1,no2:no1+no2,lst)
print(sum)

#min
min=reduce(lambda no1,no2:no1 if no1<no2 else no2,lst )
print(min)

#max
max=reduce(lambda no1,no2:no1 if no1>no2 else no2,lst)
print(max)



#find min of even numbers from list
minum=reduce(lambda num1,num2: num1 if num1<num2 else num2 , list(filter(lambda num:num%2==0,lst)))
print(minum)