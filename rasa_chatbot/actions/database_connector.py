import sqlite3

conn = sqlite3.connect('name.db')

c = conn.cursor()

# c.execute("""CREATE TABLE usernames(
#             n text
#          )""")

c.execute("""INSERT INTO usernames VALUES(
            'phanikiran'
         )""")

c.execute("SELECT * FROM usernames")

print(c.fetchone())

conn.commit()

conn.close()