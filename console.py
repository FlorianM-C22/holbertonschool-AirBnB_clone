#!/usr/bin/python3
"""HBNBCommand class module"""

import cmd
from models import storage
from models.base_model import BaseModel
CLASS_NAMES = [
    'BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review'
    ]


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
        args_list = arg.split()
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
        """
        Prints the string representation of an instance
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in CLASS_NAMES:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            instances = storage.all()
            key = "{}.{}".format(class_name, args[1])
            if key not in instances:
                print("** no instance found **")
                return
            print(instances[key])
        except Exception as e:
            print(f"Error: {e}")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in CLASS_NAMES:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            instances = storage.all()
            key = "{}.{}".format(class_name, args[1])
            if key not in instances:
                print("** no instance found **")
                return
            del instances[key]
            storage.save()
        except Exception as e:
            print(f"Error: {e}")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        """
        args = arg.split()
        try:
            instances = storage.all()
            if not arg:
                print([str(value) for value in instances.values()])
                return
            if args[0] not in CLASS_NAMES:
                print("** class doesn't exist **")
                return
            print([str(value) for key, value in instances.items() if args[0] in key])
        except Exception as e:
            print(f"Error: {e}")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in CLASS_NAMES:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            instances = storage.all()
            key = "{}.{}".format(class_name, args[1])
            if key not in instances:
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            setattr(instances[key], args[2], args[3].strip('"'))
            storage.save()
        except Exception as e:
            print(f"Error: {e}")


if __name__ == '__main__':
    try:
        HBNBCommand().cmdloop()
    except KeyboardInterrupt:
        pass
