

36 changes: 36 additions & 0 deletions 36
jj.py
Original file line number 	Diff line number 	Diff line change
@@ -0,0 +1,36 @@
import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS table1 (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS table2 (
        id INTEGER PRIMARY KEY,
        city TEXT,
        population INTEGER,
        area REAL,
        country TEXT
    )
''')
cursor.execute('''
    INSERT INTO table1 (name, age) VALUES
        ('Alice', 25),
        ('Bob', 30),
        ('Charlie', 22)
''')
cursor.execute('''
    INSERT INTO table2 (city, population, area, country) VALUES
        ('New York', 8537673, 468.9, 'USA'),
        ('Tokyo', 9273000, 622.99, 'Japan'),
        ('London', 8982000, 1572, 'UK')
''')
conn.commit()
conn.close()

print("База данных успешно создана и заполненa!")
