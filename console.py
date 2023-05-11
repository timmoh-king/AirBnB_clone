#!/usr/bin/python3

"""
    a program called console.py
    that contains the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
        Entry point of the command interpreter
        The help command is built into Cmd
    """
    prompt = '(hbnb)'

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
