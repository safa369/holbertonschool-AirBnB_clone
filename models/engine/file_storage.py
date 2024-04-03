#!/usr/bin/python3
"""Class creation to define attrs/methods of the console"""
from os import path
import json
from models.base_model import BaseModel


class FileStorage:
    """Class FileStorage to define attrs/methods"""

    """Private class attributes"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionaty '__objects'"""
        return self.__objects

    def new(self, obj):
        """Sets in '__objects' the object with the key """
        key = self.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes '__objects' dictionary to a JSON file"""
        data = {key: value.to_dict() if isinstance(value, BaseModel) else value
                for key, value in self.__objects.items()}
        with open(self.__file_path, mode='w') as file:
            json.dump(data, file)

    def reload(self):
        """Deserializes the JSON file to __objects' dictionary'"""
        if path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                self.__objects = json.loads(file.read())
