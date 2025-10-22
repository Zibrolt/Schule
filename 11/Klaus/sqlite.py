import sqlite3

connection = sqlite3.connect("meine_datenbank.db")
cursor = connection.cursor()

"""
sql =   "CREATE TABLE kunde(" \
        "kdn INTEGER PRIMARY KEY AUTOINCREMENT," \
        "vorname TEXT," \
        "nachname TEXT," \
        "age INTEGER," \
        "email TEXT" \
        ")"
cursor.execute(sql)

sql =   "INSERT INTO kunde VALUES(" \
        "1000, 'Karl', 'Mayr', 34, 'karl@mayr.de'" \
        ")"
cursor.execute(sql)

sql =   "INSERT INTO kunde(vorname, nachname, age, email) VALUES(" \
        "'Maria', 'Habermann', 55, 'mariah@gmx.de'" \
        ")"
cursor.execute(sql)
connection.commit()
"""

sql =   "SELECT *" \
        "FROM kunde"
result = cursor.execute(sql)


for row in result:
    print([val for val in row])
connection.close()