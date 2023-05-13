#!/usr/bin/python3

"""
    a program called console.py
    that contains the entry point of the command interpreter
"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    """split arguments in bits"""
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """
        Entry point of the command interpreter
        The help command is built into Cmd
    """
    prompt = '(hbnb)'
    __classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
        }

    def emptyline(self):
        """Do nothing upon receiving an empty line"""
        pass

    def do_create(self, arg):
        """Create a new class instance and print its id"""
        arg_len = parse(arg)
        if len(arg_len) == 0:
            print("** class name missing **")
        elif arg_len[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg_len[0])().id)
            storage.save()

    def do_show(self, arg):
        """Disp the str rep of a class instance of a given id"""
        arg_len = parse(arg)
        obj_dict = storage.all()
        if len(arg_len) == 0:
            print("** class name missing **")
        elif arg_len[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_len) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_len[0], arg_len[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arg_len[0], arg_len[1])])

    def do_destroy(self, arg):
        """Delete a clas instance given an id"""
        arg_len = parse(arg)
        obj_dict = storage.all()
        if len(arg_len) == 0:
            print("** class name missing **")
        elif arg_len[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_len) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_len[0], arg_len[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(arg_len[0], arg_len[1])]
            storage.save()

    def do_all(self, arg):
        """Display string representations of all inst of a given cls"""
        arg_len = parse(arg)
        if len(arg_len) > 0 and arg_len[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj_len = []
            for obj in storage.all().values():
                if len(arg_len) > 0 and arg_len[0] == obj.__class__.__name__:
                    obj_len.append(obj.__str__())
                elif len(arg_len) == 0:
                    obj_len.append(obj.__str__())
            print(obj_len)

    def do_count(self, arg):
        """Retrieve the number of instances of a given class"""
        arg_len = parse(arg)
        count = 0
        for obj in storage.all().values():
            if arg_len[0] == obj.__class.__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """
            Update a class instance of a given id by adding or updating
            a given attribute key/value pair or dictionary.
        """
        arg_len = parse(arg)
        obj_dict = storage.all()
        if len(arg_len) == 0:
            print("** class name missing **")
            return False
        if arg_len[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arg_len) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_len[0], arg_len[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(arg_len) == 1:
            print("** attribute name missing **")
            return False
        if len(arg_len) == 3:
            try:
                type(eval(arg_len[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg_len) == 4:
            obj = obj_dict["{}.{}".format(arg_len[0], arg_len[1])]
            if arg_len[2] in obj.__class__.__dict__.keys():
                value_type = type(obj.__class__.__dict__[arg_len[2]])
                obj.__dict__[arg_len[2]] = value_type(arg_len[3])
            else:
                obj.__dict__[arg_len[2]] = arg_len[3]

        elif type(eval(arg_len[2])) == dict:
            obj = obj_dict["{}.{}".format(arg_len[0], arg_len[1])]
            for k, v in eval(arg[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    value_type = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = value_type(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
