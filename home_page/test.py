import psycopg2
import psutil
con = psycopg2.connect(
  database="tredebot_db",
  user="tredebot",
  password="1234567890lP",
  host="127.0.0.1",
  port="5432"
)

print("Database opened successfully")
cur = con.cursor()
cur.execute( "SELECT   id_pid FROM home_page_idpid")
rows = cur.fetchall()
pid_id = (rows[-1][0])
print(pid_id)
p = psutil.Process(pid_id)
p.kill()

cur = con.cursor()
cur.execute("SELECT sum_client,who_client_id,date_client from home_page_summclientitog")
# cur.execute ("select username from  auth_user where id =(%i)"%a)
rows = cur.fetchall()
user = rows[0]

sum=(user[0])
id = user[1]
cur = con.cursor()
cur.execute("DELETE from home_page_summclientitog")
cur = con.cursor()

cur.execute ("SELECT username FROM auth_user where id =%s" % id)
itog = cur.fetchall()
client =((itog[0])[0])
print(client)
x = str(sum)
id_itog = str(id)

cur = con.cursor()
cur.execute(
"INSERT INTO home_page_historyclient (summ_history_client,who_id,date) VALUES (%s,%s,now()) RETURNING id" %(x,id_itog)

)
end = cur.fetchall()
end_itog = str((end[0])[0])
print (end_itog)

cur = con.cursor()
cur.execute("DELETE from home_page_summclientitog")


cur = con.cursor()
cur.execute(
  """UPDATE home_page_historyclient
  SET data_end = now()
  WHERE id =(%s)
  """ % (end_itog)

)
# # con.commit()
# # con.close()
con.commit()
con.close()