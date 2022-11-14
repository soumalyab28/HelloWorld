import datetime
from datetime import date, timedelta
import cx_Oracle
import time

start = time.time()

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

connection_dest = cx_Oracle.connect(user="soum",password="soum",dsn="localhost/xepdb1")
connection_src = cx_Oracle.connect(user="soum",password="soum",dsn="localhost/soum_pdb1")
# time.sleep(8)
# print("Successfully connected to Oracle Database")

cursor_src = connection_src.cursor()
cursor_dest = connection_dest.cursor()
rows = []
cursor_dest.execute('truncate table employees')

start_date = date(2022, 8, 1)
end_date = date(2022, 9, 9)
for single_date in daterange(start_date, end_date):
    v_sql = "select /*+parallel*/ * from employees where batch_date = to_date('"+str(single_date)+"','YYYY-MM-DD')"
    for row in cursor_src.execute(v_sql):
        rows.append(row)
    cursor_dest.executemany("""Insert /*+APPEND*/ into EMPLOYEES Values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11)""",rows)
    connection_dest.commit()
    rows = []

end = time.time()

print("The time of execution of above program is :", (end-start), " seconds")