#!/usr/bin/python3
"""
Console Module
"""
import cmd
import sys
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Console class
    """
    prompt = "(hbnb) "
    class_dict = {
        "BaseModel": BaseModel,
    }

    def do_quit(self, arg):
        """
        Exit command interpreter
        """
        sys.exit()

    def do_EOF(self, arg):
        """
        Handles EOF
        """
        print()
        return True

    def emptyline(self):
        """
        Handles empty line
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel
        """
        args_list = shlex.split(arg)
        if len(args_list) == 0:
            print("** class name missing **")
            return
        else:
            class_name = args_list[0]
            if class_name not in HBNBCommand.class_dict:
                print("** class doesn't exist **")
                return
            else:
                obj = HBNBCommand.class_dict[class_name]()
                storage.new(obj)
                storage.save()
                print(obj.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        """
        args_list = shlex.split(arg)
        if not args_list:
            print("** class name missing **")
            return
        try:
            class_name = args_list[0]
            if class_name not in HBNBCommand.class_dict:
                print("** class doesn't exist **")
                return
            if len(args_list) < 2:
                print("** instance id missing **")
                return
            instances = storage.all()
            key = "{}.{}".format(class_name, args_list[1])
            if key not in instances:
                print("** no instance found **")
                return
            print(instances[key])
        except Exception:
            pass

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
            if class_name not in storage.classes():
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
        except Exception:
            pass

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        """
        args = arg.split()
        instances = storage.all()
        if not arg:
            print([str(value) for value in instances.values()])
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        print([str(value) for key, value in instances.items()
               if args[0] in key])

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
            if class_name not in storage.classes():
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
        except Exception:
            pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
