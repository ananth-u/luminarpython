from functools import*
isl=[
{"team_name":"mumbaicity","mp":7,"win":5,"drawn":1,"loss":1,"gf":11,"ga":3,"pts":16},
{"team_name":"atk","mp":7,"win":5,"drawn":1,"loss":1,"gf":8,"ga":3,"pts":16},
{"team_name":"benguluru","mp":7,"win":3,"drawn":3,"loss":1,"gf":11,"ga":8,"pts":12},
{"team_name":"northeast","mp":7,"win":2,"drawn":4,"loss":1,"gf":8,"ga":6,"pts":10},
{"team_name":"jemshedh","mp":7,"win":2,"drawn":4,"loss":1,"gf":8,"ga":7,"pts":10}

]

#print team anems in uppercase:
upp=list(map(lambda team:team["team_name"].upper(),isl))
print(upp)

#highest point:
point=reduce(lambda no1,no2:no1 if no1>no2 else no2,list(map(lambda team:team["pts"],isl)))
print(point)
teamname=list(filter(lambda team:team["pts"]==point,isl))
for team in teamname:
    print(team["team_name"])

#min point
minum=reduce(lambda no1,no2:no1 if no1<no2 else no2,list(map(lambda team:team["pts"],isl)))
print(minum)

#highest win team
high=reduce(lambda no1,no2:no1 if no1>no2 else no2,list(map(lambda team:team["win"],isl)))
teamname=list(filter(lambda team:team["win"]==high,isl))
print(teamname)