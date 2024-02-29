#!/usr/bin/python3
"""
BaseModel class module


"""

import uuid
import datetime


class BaseModel:
    """
    Base class for other classes to be used in the project
    """
    def __init__(self):
        """
        Constructor for the BaseModel class
        """
        self.updated_at = datetime.datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()

    def __str__(self):
        """
        Returns a string representation of the object
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """
        Updates the public instance attribute updated_at with the current
        datetime
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the
        instance
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["created_at"] = self.created_at.isoformat()
        return new_dict
