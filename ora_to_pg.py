import psycopg2
import oracledb
import time

start = time.time()

con_pg = psycopg2.connect(database = "soum_xepdb1", user = "postgres", password = "soum", host = "localhost", port = '5432')
cur_pg = con_pg.cursor()

connection_dest = oracledb.connect(user="soum",password="soum",dsn="localhost/xepdb1")
cursor_dest = connection_dest.cursor()

pool = oracledb.SessionPool

cursor_dest.execute('select count(*) from employees')
row_cnt_oracle = cursor_dest.fetchall()

# To ensure clean data load we will truncate the Postgres 
cur_pg.execute('truncate table employees')

for row in cursor_dest.execute('select /*+parallel*/ * from employees'):
    # rows.append(row)
    cur_pg.execute('insert into employees values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',row)

# for row in rows:
#     cur_pg.execute('insert into employees (emp_id,salutation,first_name,middle_name,last_name,end_dt) values (%s,%s,%s,%s,%s,%s)',row)
#     # cur_pg.commit()

# cur_pg.execute('insert into employees (emp_id,salutation,first_name,middle_name,last_name) values (%s,%s,%s,%s,%s)',rows)

cur_pg.execute("select count(*) from employees")
# rows = []
row_cnt_pg = cur_pg.fetchall()
# for row in cur_pg.execute("select emp_id,salutation,first_name,middle_name,last_name from employees"):
    # result = cur_pg.fetchall()
    # rows.append(row)

if row_cnt_oracle == row_cnt_pg:
    print("Datacopy successful",row_cnt_oracle[0][0])

end = time.time()
print("Time taken :", (end-start), " seconds")

# cur_pg.execute("select * from employees limit 5")
# print(cur_pg.fetchall())