#!/usr/bin/python3
"""Class creation to define attrs/methods of the console"""
import json
import os
from datetime import datetime


class FileStorage:
    """Class FileStorage to define attrs/methods"""

    """Private class attributes"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionaty '__objects'"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in '__objects' the object with the key """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes '__objects' dictionary to a JSON file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            data = {key: value.to_dict() for key,
                    value in FileStorage.__objects.items()}
            json.dump(data, file)

    def reload(self):
        """Deserializes the JSON file to __objects' dictionary'"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {key: self.classes()[value["__class__"]](**value)
                        for key, value in obj_dict.items()}
            FileStorage.__objects = obj_dict

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes


def attributes(self):
    """Returns the valid attributes
    and their types for classname"""
    attributes = {
            "BaseModel":
            {"id": str,
             "created_at": datetime.datetime,
             "updated_at": datetime.datetime},
            "User":
            {"email": str,
             "password": str,
             "first_name": str,
             "last_name": str},
            "State":
            {"name": str},
            "City":
            {"state_id": str,
             "name": str},
            "Amenity":
            {"name": str},
            "Place":
            {"city_id": str,
             "user_id": str,
             "name": str,
             "description": str,
             "number_rooms": int,
             "number_bathrooms": int,
             "max_guest": int,
             "price_by_night": int,
             "latitude": float,
             "longitude": float,
             "amenity_ids": list},
            "Review":
            {"place_id": str,
             "user_id": str,
             "text": str}
        }
    return attributes
