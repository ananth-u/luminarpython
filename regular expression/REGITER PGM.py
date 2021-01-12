from re import*

f=open("registrationnumbers","r")
fout=open("validreg","w")

regnum=set()
for numbers in f:
    regnum.add(numbers.rstrip("\n"))


rule="KL\d{2}[A-Z]{1,2}\d{1,4}"

for vehnum in regnum:

    matcher=fullmatch(rule,vehnum)
    if matcher !=None:
      fout.write(vehnum+"\n")
    else:
      print("invalid")