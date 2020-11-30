employees=[

    [1001,"ajay","qa",1981,2003],
    [1002,"vijay","developer",1992,2008],
    [1003,"arun","ba",1989,2010],
    [1004,"amal","developer",2009,2014],
    [1005,"vimal","developer",1987,1989]
]

#print all employee desigination
for emp in employees:
    print(emp[2])
print()
#print all employees whose desi=developer
for emp in employees:
    if emp[2]=="developer":
        print(emp)
print()
#print all employees those who are working in 1980's
for emp in employees:
    if ((emp[3] in range(1980,1990)) & (emp[4] in range(1980,1990))):
        print(emp)
print()
#print all employees details whose experience >9 yrs
for emp in employees:
    if (emp[4]-emp[3])>9 :
        print(emp)
