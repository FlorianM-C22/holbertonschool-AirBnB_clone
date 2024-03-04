#!/usr/bin/python3
"""
Console Module
"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Console class
    """
    prompt = "(hbnb) "

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
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

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
