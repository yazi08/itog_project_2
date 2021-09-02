from home_page.sql_connect import SqlConnect
import psutil
import os
import psycopg2

pid = os.getpid()
print (pid)
a = str(pid)
# p = psutil.Process(pid)
# p.kill()

connection = SqlConnect()


connection.connect().execute(
"INSERT INTO home_page_idpid (id_pid) VALUES (%s) " % a)

connection.commit_sql()
connection.close_sql()

# cur = con.cursor()
# cur.execute("SELECT sum_client,who_client_id from home_page_summclientitog")
#
# # cur.execute ("select username from  auth_user where id =(%i)"%a)
# rows = cur.fetchall()
