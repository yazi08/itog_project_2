# import psycopg2
# import telebot
# con = psycopg2.connect(
#   database="tredebot_db",
#   user="tredebot",
#   password="1234567890lP",
#   host="127.0.0.1",
#   port="5432"
# )
# cur = con.cursor()
# cur.execute("SELECT  summ_history_client from home_page_historyclient ORDER BY id DESC LIMIT 1")
# # cur.execute ("select username from  auth_user where id =(%i)"%a)
# rows = cur.fetchall()
# summ = rows[0][0]
# print(summ)
# con.commit()
# con.close()
# a = f"Cумма достигла {summ}"
#
# bot = telebot.TeleBot('1724798563:AAFy0nHNECc3JL1ZnDCC_hXqnQVy8cV76LU')
# @bot.message_handler(commands=['start'])
# def start_command(message):
#     bot.send_message(message.chat.id, a)


