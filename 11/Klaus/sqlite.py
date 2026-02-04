import sqlite3

def init_db():
    with sqlite3.connect("adressen.db") as conn:
        cursor = conn.cursor()
        sql = """
            CREATE TABLE IF NOT EXISTS adressen (
            adress_id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            street TEXT NOT NULL,
            postalcode TEXT NOT NULL,
            city TEXT NOT NULL,
            phone TEXT
            )
            """
        cursor.execute(sql)

def add_address(fname, lname, street, pc, city, tel):
    with sqlite3.connect("adressen.db") as conn:
        cursor = conn.cursor()
        sql = """
            INSERT INTO adressen (
                firstname,
                lastname,
                street,
                postalcode,
                city,
                phone
                )
                VALUES (?, ?, ?, ?, ?, ?)
            """
        
        if check_adress(fname, lname, street, pc, city, tel):
            return
        cursor.execute(sql, (fname, lname, street, pc, city, tel))

def check_adress(fname, lname, street, pc, city, tel):
    with sqlite3.connect("adressen.db") as conn:
        cursor = conn.cursor()
        sql = f"""
            SELECT 1
            FROM adressen
            WHERE firstname = ?
            AND lastname = ?
            AND street = ?
            AND postalcode = ?
            AND city = ?
            AND phone = ?
            """ 
        res = cursor.execute(sql, (fname, lname, street, pc, city, tel)).fetchone()
        return res is not None


def remove_address(fname, lname, street, pc, city, tel):
    with sqlite3.connect("adressen.db") as conn:
        cursor = conn.cursor()
        sql = f"""
            DELETE FROM adressen
            WHERE firstname = ?
            AND lastname = ?
            AND street = ?
            AND postalcode = ?
            AND city = ?
            AND phone = ?
            """ 
        cursor.execute(sql, (fname, lname, street, pc, city, tel))

def read_all():
    with sqlite3.connect("adressen.db") as conn:
        cursor = conn.cursor()
        sql = """
            SELECT * FROM adressen
            """
        cursor.execute(sql)
        ergebnis = cursor.fetchall()
    return ergebnis

init_db()
add_address("Peter", "Mayr", "Auerswaldweg 5", "85058", "Ingolstadt", "")
add_address("Maria", "Unterforstheimer", "Adlerweg 3", "85118", "Walting", "+491708934788")
add_address("Anna", "Karenina", "Ostwall 17", "09782", "Potsdam", "03054506767")

print(read_all())