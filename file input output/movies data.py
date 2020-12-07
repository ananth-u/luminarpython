#find the movies year wise release count

f=open("movies.csv","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    year=data[2]
    if year not in dict:
        dict[year]=1
    else:
        dict[year]+=1

print(dict)

#whic year highest number of movies realaesed

high=max(dict,key=dict.get)
print(high,"has highest number of movies",dict[high])