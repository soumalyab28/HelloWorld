import cx_Oracle
# import config
import time
from tabulate import tabulate
table = [['First Name', 'Last Name']]

connection = cx_Oracle.connect(user="soum",password="soum",dsn="localhost/xepdb1")

# time.sleep(8)
# print("Successfully connected to Oracle Database")

cursor = connection.cursor()

# # Create a table

# cursor.execute("""
#     begin
#         execute immediate 'drop table todoitem';
#         exception when others then if sqlcode <> -942 then raise; end if;
#     end;""")

# cursor.execute("""
#     create table todoitem (
#         id number generated always as identity,
#         description varchar2(4000),
#         creation_ts timestamp with time zone default current_timestamp,
#         done number(1,0),
#         primary key (id))""")

# # Insert some data

# rows = [ ("Task 1", 0 ),
#          ("Task 2", 0 ),
#          ("Task 3", 1 ),
#          ("Task 4", 0 ),
#          ("Task 5", 1 ) ]

# cursor.executemany("insert into todoitem (description, done) values(:1, :2)", rows)
# print(cursor.rowcount, "Rows Inserted")

# connection.commit()


# Now query the rows back
for row in cursor.execute('select First_Name, Last_name from CUStomer'):
    table.append(row)

# print(tabulate(table))
print("\n")
print(tabulate(table, headers="firstrow",tablefmt="grid"))