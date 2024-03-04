#!/usr/bin/python3
"""FileStorage class module"""

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
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        dict_serialize = {}
        for key, value in self.__objects.items():
            dict_serialize[key] = value.to_dict

        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(dict_serialize, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass
