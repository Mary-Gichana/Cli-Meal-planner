import sqlite3
from app import DATABASE_NAME

class MealCategory:
    def __init__(self, name, id= None):
        self.id = id  
        self.name = name

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        if isinstance(id, int):
            self._id = id
        else:
            raise ValueError("ID must be an integer")
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            raise ValueError("Name must be a string")
    def __repr__(self):
        return f"MealCategory({self._id}, {self._name})"
    
    @classmethod
    def add_category(cls, name):
        
            with sqlite3.connect(DATABASE_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO mealcategory (name) VALUES (?)', (name,))
                conn.commit()
    @classmethod
    def delete_category(cls, name):
        
            with sqlite3.connect(DATABASE_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM mealcategory WHERE name = ?', (name,))
                conn.commit()

    @classmethod
    def find_all(cls):
        
            with sqlite3.connect(DATABASE_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM mealcategory')
                categories = cursor.fetchall()
                return categories
    @classmethod
    def find_by_name(cls, name):
        
            with sqlite3.connect(DATABASE_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM mealcategory WHERE name = ?', (name,))
                category = cursor.fetchone()
                return category
    @classmethod
    def find_by_id(cls, category_id):
        
            with sqlite3.connect(DATABASE_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM mealcategory WHERE id = ?', (category_id,))
                category = cursor.fetchone()
                return category

