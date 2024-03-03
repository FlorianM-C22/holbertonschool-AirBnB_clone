#!/usr/bin/python3
"""
-
FileStorage class module
-
"""

import json


class FileStorage:
    """
    FileStorage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the __objects dictionnary
        """
        return self.__objects

    def new(self, obj):
        """
        Sets obj in __objects
        """
        key = f"{obj.__class__.__name__}obj.id"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        try:
            if self.__file_path is not None:
                with open("__file_path", "r", encoding="utf-8") as f:
                    json.load(self.__object, f)
        except FileNotFoundError:
            pass
