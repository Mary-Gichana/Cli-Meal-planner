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
    


    