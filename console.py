#!/usr/bin/python3
"""HBNBCommand class module"""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = '(hbnb) '
    class_dict = {
        "BaseModel": BaseModel,
        #"User": User,
        #"State": State,
        #"City": City,
        #"Amenity": Amenity,
        #"Place": Place,
        #"Review": Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF (Ctrl + D)."""
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and prints the id."""
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
