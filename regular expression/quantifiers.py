#quantifiers : houw much number of

from re import*

#pattern="a+" #check for a and more than one a
#pattern="a*"  #check for a+ and zro curences of a
#pattern="a?"   #a and zero number of a
pattern="^a" #check fo starting with a
#pattern="a$" #ending with a
#pattern='a{2,3}' #check for minum 2 a and max 3 a

#matcher=finditer(pattern,"aaaabaabaaaaa")
#for match in matcher:
 #   print(match.start())
  #  print(match.group())


matcher=fullmatch(pattern,"baaaabaabaab")
if matcher!=None:
    print("given starting wit a")
else:
    print("not startin with a")
