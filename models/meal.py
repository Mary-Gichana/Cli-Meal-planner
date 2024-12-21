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

    