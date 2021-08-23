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
cur.execute("SELECT sum_client from home_page_summclientitog")

rows = cur.fetchall()
a = rows[0]
y = list(a)
print (y)
b = (y[0])
print (b)
print(type(b))
x = str(b)
print(type(x))


cur = con.cursor()
cur.execute(
  "INSERT INTO History (summ) VALUES (80000)"
)
cur = con.cursor()
cur.execute("DELETE from home_page_summclientitog")
con.commit()
con.close()
print (x)

