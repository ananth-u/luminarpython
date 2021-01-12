from dbconnectprgm.dbconnect import *

db=get_connection()
cursor=db.cursor()
id=input("enter id")
name=input("enter name")
subject=input("enetr subject")

for i in range(0,10):

  sql="insert into  faculty(id,name,subject)values('100','ajay','datastructure')"

  try:
    cursor.execute(sql)
    db.commit()
    print("query executed")

  except Exception as e:
    print(e.args)

  finally:
    db.close()
