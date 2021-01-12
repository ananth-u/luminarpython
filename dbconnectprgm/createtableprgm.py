


#wwe need database connection

from dbconnectprgm.dbconnect import *

db=get_connection()

cursor=db.cursor()

sql="create table faculty(id varchar(20),name varchar(25),subject varchar(50)) "
try:
    cursor.execute(sql)
    print("table successfully created")

except Exception as e:
    print(e.args)

finally:
    db.close()
