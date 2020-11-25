lowlimt=int(input("enetr value"))
upperlimit=int(input("enetr value"))

for j in range (lowlimt,(upperlimit+1)):

  for i in range(2,j):
    if(j%i==0):

        break

  else:
         print(j)