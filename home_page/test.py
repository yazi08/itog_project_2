import psycopg2




con = psycopg2.connect(
  database="tredebot_db",
  user="tredebot",
  password="1234567890lP",
  host="127.0.0.1",
  port="5432"
)

print("Database opened successfully")


cur = con.cursor()
cur.execute("SELECT sum_client,who_client_id from home_page_summclientitog")

# cur.execute ("select username from  auth_user where id =(%i)"%a)
rows = cur.fetchall()
user = rows[0]
print (rows)

sum=user[0]
id = user[1]


print (id)
# r = str(id)
# print (type(r))
cur.execute ("SELECT username FROM auth_user where id =%s" % id)
itog = cur.fetchall()
client =((itog[0])[0])


x = str(sum)
id_itog = str(id)

cur = con.cursor()
cur.execute(
"INSERT INTO home_page_historyclient (summ_history_client,who_id,date) VALUES (%s,%s,now())" %(x,id_itog)

)

cur = con.cursor()
cur.execute("DELETE from home_page_summclientitog")
con.commit()
con.close()





