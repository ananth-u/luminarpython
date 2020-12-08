f=open("covid 19 .csv","r")


covid={}
for lines in f:

    sno,date,time,state,cnfiindian,cnfirmnforegn,cured,deaths,confirmed=lines.rstrip("\n").split(",")
    covid[state]={"state":state,"cured":cured,"deaths":deaths,"confirmed":confirmed}

for k,v in covid.items():

  print(k,v)



def print_covid(**kwargs):

    state = kwargs["state"]
    if state in covid:
        print(state,",",covid[state]["confirmed"])
        prop = kwargs["property"]
        if prop in covid[state]:
            print("deaths", covid[state][prop])
        else:
            print("invalid property")
    else:
        print("invalid id")


print_covid(state="Kerala", property="deaths")
