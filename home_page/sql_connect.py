import psycopg2

class SqlConnect:

    def __init__(self):


        self.con = psycopg2.connect(
            database="tredebot_db",
            user="tredebot",
            password="1234567890lP",
            host="127.0.0.1",
            port="5432"
        )

    def connect(self):
        cur = self.con.cursor()
        return cur


    def commit_sql(self):
        sql_commit = self.con.commit()

        return sql_commit

    def close_sql(self):
        sql_close= self.con.close()

        return sql_close



# cur = con.cursor()
# cur.execute("SELECT sum_client,who_client_id from home_page_summclientitog")
#
# # cur.execute ("select username from  auth_user where id =(%i)"%a)
# rows = cur.fetchall()


if __name__ =='__main__':
    s = SqlConnect()
    s.connect()