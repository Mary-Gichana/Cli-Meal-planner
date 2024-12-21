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
