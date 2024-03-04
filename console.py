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

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in globals() or not issubclass(globals()[args[0]],
                                                        BaseModel):
            print("** class doesn't exist **")
        else:
            new_instance = globals()[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in globals() or not issubclass(globals()[args[0]],
                                                        BaseModel):
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in globals() or not issubclass(globals()[args[0]],
                                                        BaseModel):
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances"""
        args = line.split()
        if len(args) > 0 and (args[0] not in globals()
                              or not issubclass(globals()[args[0]],
                                                BaseModel)):
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                if len(args) == 0 or key.split('.')[0] == args[0]:
                    print(str(value))

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in globals() or not issubclass(globals()[args[0]],
                                                        BaseModel):
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            attr = args[2]
            value = args[3]
            if attr not in ['id', 'created_at', 'updated_at']:
                if value.isdigit():
                    value = int(value)
                elif '.' in value and all(v.isdigit() for v in value.split('.')):
                    value = float(value)
                else:
                    value = str(value)
                setattr(storage.all()[key], attr, value)
                storage.save()


if __name__ == '__main__':
    try:
        HBNBCommand().cmdloop()
    except KeyboardInterrupt:
        pass
