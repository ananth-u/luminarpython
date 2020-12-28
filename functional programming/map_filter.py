lst=[10,20,30]

#square of the number
#map():

square=list(map(lambda num:num**2,lst))
print(square)


#filter(():
even=list(filter(lambda num:num%2==0,lst))
print(even)