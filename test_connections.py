import cx_Oracle
import psycopg2

con_pg = psycopg2.connect(database = "soum_xepdb1", user = "postgres", password = "soum", host = "localhost", port = '5432')
cur_pg = con_pg.cursor()

connection_dest = cx_Oracle.connect(user="soum",password="soum",dsn="localhost/xepdb1")
cursor_dest = connection_dest.cursor()

sql = """select * from employees"""

cursor_dest.execute(sql + " where rownum < 5")
ora_results = cursor_dest.fetchall()

cur_pg.execute(sql + " limit 5")
pg_results = cur_pg.fetchall()

# print(ora_results)
print(pg_results)