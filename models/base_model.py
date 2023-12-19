#!/usr/bin/python3
"""model that defines all common attributes/ methods of other classes"""

from uuid import uuid4
from datetime import datetime


class BaseModel():
    """a class base model that defines all common attributes/methods
    Attributes:
            id: the id of each basemodel (string).
            created_at: the date and time when the instance is created.
            updated_at: the date and time when the instance is apdated."""

    def __init__(self):
        """assign the attributes"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """return the infrmation n human readable"""
        return ("[{}] {} {}"
                .format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """save the current datetime of the updates """
        updated_at = datetime.now()

    def to_dict(self):
        """return a dictionary containig all key and value of the instance"""
        dict_f = {}
        dict_f["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                dict_f[key] = value.isoformat()
            else:
                dict_f[key] = value
        return dict_f
