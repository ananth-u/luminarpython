students=[

    [100,"arjun","bca",45],
    [101, "ananthu", "bca", 150],
    [102, "achu", "mca", 200],
    [103, "jeetu", "mca", 400],
    [104, "kichu", "bcom", 70],

]

#print student names

for student in students:
  print(student[1])

#print total of all students

total=0
for student in students:
  total=total+student[3]
print(total)

#list destails of student whose corse mca

for student in students:
   if student[2]=='mca':
      print(student)


#mca? bca? bcom?
bcasum=0
mcasum=0
bcomsum=0
for student in students:
    if student[2]=='bca':
        bcasum=bcasum+1

    elif student[2]=='mca':
          mcasum = mcasum + 1
    elif student[2]=='bcom':
         bcomsum=bcomsum+1

print(bcasum,",",mcasum,",",bcomsum)

#print("highest number of students",max(bcasum,mcasum,bcomsum))


if ((bcasum>mcasum) & (bcasum>bcomsum)):
    print("bca has the highest number of students", bcasum)

elif ((mcasum>bcasum) & (mcasum>bcomsum)):
    print("mca has the highest number of students", mcasum)


elif ((bcomsum>bcasum) & (bcomsum>mcasum)):
    print("bcom has the highest number of students", bcomsum)

elif bcomsum==mcasum:
    print("bcom and mca hast highest number of students",bcomsum)
    
elif   bcomsum==bcasum:
    print("bcom and bca hast highest number of students", bcomsum)

elif mcasum==bcasum:
    print("bca and mca hast highest number of students", mcasum)

