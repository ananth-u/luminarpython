
from re import*
rule="KL\d{2}[A-Z]{2}\d{1,4}"

number=input("enter")
matcher=fullmatch(rule,number)
if matcher !=None:
    print("valid")
else:
    print("invalid")