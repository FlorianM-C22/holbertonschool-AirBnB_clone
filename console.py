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
        # "User": User,
        # "State": State,
        # "City": City,
        # "Amenity": Amenity,
        # "Place": Place,
        # "Review": Review
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

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id."""
        args_list = shlex.split(arg)
        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
        elif len(args_list) == 1:
            print("** instance id missing **")
        else:
            key = args_list[0] + "." + args_list[1]
            obj = storage.all()
            if key in obj:
                print(obj[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args_list = shlex.split(arg)
        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
        elif len(args_list) == 1:
            print("** instance id missing **")
        else:
            key = args_list[0] + "." + args_list[1]
            obj = storage.all()
            if key in obj:
                del (obj[key])
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation"""
        args_list = shlex.split(arg)
        obj_list = []
        if len(args_list) == 0:
            for obj in storage.all().value():
                obj_list.append(str(obj))
            print(obj_list)
        elif args_list[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
        else:
            cls_name = args_list[0]
            for key, obj in storage.all().items():
                if type(obj).__name__ == cls_name:
                    obj_list.append(str(obj))
            print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args_list = shlex.split(arg)
        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
        elif len(args_list) == 1:
            print("** instance id missing **")
        elif len(args_list) == 2:
            print("** attribute name missing **")
        elif len(args_list) == 3:
            print("** value missing **")
        elif len(args_list) > 3:
            key = args_list[0] + "." + args_list[1]
            obj = storage.all()
            if key in obj:
                try:
                    if args_list[2] not in obj[key].__dict__:
                        obj[key].__dict__[args_list[2]] = args_list[3]
                    else:
                        value = type(getattr(obj[key], args_list[2]))
                        (args_list[3])
                        setattr(obj[key], args_list[2], value)
                    obj[key].save()
                except AttributeError:
                    pass
            else:
                print("** no instance found **")


if __name__ == '__main__':
    try:
        HBNBCommand().cmdloop()
    except KeyboardInterrupt:
        pass
