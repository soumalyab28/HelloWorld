import cx_Oracle
# import config
import time
from tabulate import tabulate
table = [['First Name', 'Last Name']]

start = time.time()

connection_dest = cx_Oracle.connect(user="soum",password="soum",dsn="localhost/xepdb1")
connection_src = cx_Oracle.connect(user="soum",password="soum",dsn="localhost/soum_pdb1")
# time.sleep(8)
# print("Successfully connected to Oracle Database")

cursor_src = connection_src.cursor()
cursor_dest = connection_dest.cursor()

rows = []
# # Insert some data

# rows = [ ("Task 1", 0 ),
#          ("Task 2", 0 ),
#          ("Task 3", 1 ),
#          ("Task 4", 0 ),
#          ("Task 5", 1 ) ]

# cursor.executemany("insert into todoitem (description, done) values(:1, :2)", rows)
# print(cursor.rowcount, "Rows Inserted")

# connection.commit()
#v_emp_id = 9338975
# v_sql = "SELECT /*+PARALLEL(16)*/ * FROM EMPLOYEES WHERE EMP_ID = "+str(v_emp_id)
# for row in cursor_src.execute(v_sql):
    # rows.append(row)

# Now query the rows back
for row in cursor_src.execute('SELECT /*+PARALLEL(16)*/ * FROM EMPLOYEES'):
    rows.append(row)
    # result = cursor_src.fecthall()
    #cursor_dest.execute("Insert into EMPLOYEES (EMP_ID,SALUTATION,FIRST_NAME,MIDDLE_NAME,CUST_ORG_NAME,NAME_TITLE,CUST_TYPE,CREATED_DT,END_DT,LAST_UPDATED_DT) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10)",rows)

# print(tabulate(table))
#print("\n")
#print(tabulate(table, headers="firstrow",tablefmt="grid"))

# for row_ins in rows:
    # cursor_dest.executemany("""Insert into EMPLOYEES (EMP_ID,SALUTATION,FIRST_NAME,MIDDLE_NAME,CUST_ORG_NAME,NAME_TITLE,CUST_TYPE,CREATED_DT,END_DT,LAST_UPDATED_DT) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10)""",row_ins)

cursor_dest.executemany("""Insert /*+APPEND*/ into EMPLOYEES values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10)""",rows)
connection_dest.commit()
end = time.time()

print("The time of execution of above program is :", (end-start), " seconds")