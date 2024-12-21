import sqlite3
from app import DATABASE_NAME
from datetime import datetime

class Meal:
    def __init__(self, name,date, mealcategory_id, id= None):
        self.id = id  
        self.name = name
        self.date = date  
        self.mealcategoryid = mealcategory_id