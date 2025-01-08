import sqlite3
from app import DATABASE_NAME
from datetime import datetime

class Meal:
    def __init__(self, name,date, mealcategory_id, id= None):
        self.id = id  
        self.name = name
        self.date = date  
        self.mealcategoryid = mealcategory_id

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
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, new_date):
        if isinstance(new_date, str):
            datetime.strptime(new_date, "%Y-%m-%d")
            self._date = new_date
        else:
            raise ValueError("Date must be in the format YYYY-MM-DD")
    def __repr__(self):
        return f"Meal({self._id}, {self._name}, {self._date}, {self.mealcategory_id})"
    
    @classmethod
    def from_db(cls, row):
        return cls(name=row[1], date=row[2], mealcategory_id=row[3], id=row[0])
    @classmethod
    def add_meal(cls, name, date, mealcategory_id):
        
            with sqlite3.connect(DATABASE_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    'INSERT INTO meals (name, date, mealcategory_id) VALUES (?, ?, ?)',
                    (name, date, mealcategory_id)
                )
                conn.commit()
    @classmethod
    def delete_meal(cls, meal_id):
        
            with sqlite3.connect(DATABASE_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM meals WHERE id = ?', (meal_id,))
                conn.commit()

    @classmethod
    def find_all(cls):

            with sqlite3.connect(DATABASE_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM meals')
                meals = cursor.fetchall()
                return meals
    @classmethod
    def find_by_id(cls, meal_id):
        
            with sqlite3.connect(DATABASE_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM meals WHERE id = ?', (meal_id,))
                meal = cursor.fetchone()
                return meal
    


    