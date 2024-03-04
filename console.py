#!/usr/bin/python3
"""HBNBCommand class module"""

import json
import os
import uuid
import cmd
import shlex
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = '(hbnb) '

    def do_quit(self):
        """Quit command to exit the program"""
        return True

    def do_EOF(self):
        """Exit the program with EOF (Ctrl + D)."""
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass

    def do_create(self, arg):
        """Creates an instance of a class"""
        args_list = shlex.split(arg)
        if len(args_list) == 0:
            print("** class name missing **")
        else:
            class_name = args_list[0]
            if class_name not in HBNBCommand.class_dict:
                print("** class doesn't exist **")
            else:
                obj = HBNBCommand.class_dict[class_name]()
                storage.new(obj)
                storage.save()
                print(obj.id)


if __name__ == '__main__':
    try:
        HBNBCommand().cmdloop()
    except KeyboardInterrupt:
        pass
