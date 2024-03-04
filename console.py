#!/usr/bin/python3
"""HBNBCommand class module"""

import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF (Ctrl + D)."""
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass


if __name__ == '__main__':
    try:
        HBNBCommand().cmdloop()
    except KeyboardInterrupt:
        pass
