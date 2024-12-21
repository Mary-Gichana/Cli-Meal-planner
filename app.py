import sqlite3

DATABASE_NAME = 'database.db'

def create_database():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS mealcategory (
                id INTEGER PRIMARY KEY ,
                name TEXT UNIQUE NOT NULL
            )
        ''')