#variable name rule :

#starting with a-k
#second character shld be a digit and divisible by 3
#followed by any nuber of characters

from re import*

rule='[a-kA-k][369][a-z-A-z0-9]*'
variablename=input("eneter")

matcher=fullmatch(rule,variablename) #fullmatch"try to appy to all athe string   #match:try to apply the patternt to start of the string
if matcher !=None:
    print("valid")
else:
    print("invalid")
