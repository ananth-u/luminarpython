from re import *

#predefined character set:

#pattern='[a-z]' #check for lowercase a to z character

#pattern='[0-9]' #check for all digits
#pattern='[^0-9]' #excpet for numbers
#pattern='[^a-z]' except lowercase characters
#pattern='[a-zA-Z]' #check for both lower and uppercase

 #lower acse uper and digit
#pattern='[a-zA-Z0-9]'

#special character
#pattern='[^a-zA-Z0-9]'

#predefined characters:
#pattern="\s" #check for spaces
#pattern="\S"  #except for spaces
#pattern="\d" #check for digits
#pattern="\D" #except digits
#pattern="\w" excpet special characters
#pattern="\W" #special characters

mather=finditer(pattern,'abc Z@7k')

for match in mather:
    print(match.start()) #print the position
    print(match.group()) #print the matching group