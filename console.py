#!/usr/bin/python3
"""Console module containing the entry point of the command interpreter."""
import cmd
from models import storage
import shlex

class HBNBCommand(cmd.Cmd):
    """Class definition for the command interpreter."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def emptyline(self):
        """Handles empty line."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel."""
        if arg == "" or arg is None:
            print("** class doesn't exist")
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        else:
            store = storage.classes()[arg]()
            store.save()
            print(store.id)

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            words = arg.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_all(self, arg):
        """Prints all the instances of a specific class\n"""

        if arg != "":
            words = arg.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                nl = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == words[0]]
                print(nl)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and the id\n"""

        line = self.command_line(arg, 4)

        """Checks the class name"""
        if not self.check_class(line[0]):
            return

        """Checks the class id"""
        if not self.check_id(line[0], line[1]):
            return

        """Checks the class attributes and its value"""
        if not self.check_attr(line[2], line[3]):
            return

        value = line[3]
        if value.isnumeric():
            value = int(value)

        key = line[0] + "." + line[1]
        setattr(storage.all()[key], line[2], value)
        storage.save()

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id\n"""

        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            words = arg.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def emptyline(self):
        """Method to cancel last command repetition"""
        pass

    def check_class(self, clsname):
        """Validations of class name existency"""
        if clsname == "":
            print("** class name missing **")
            return False
        elif clsname not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        return True

    def check_id(self, clsname, id):
        """Validations of id existency"""
        if id == "":
            print("** instance id missing **")
            return False
        elif clsname + "." + id not in storage.all():
            print("** no instance found **")
            return False
        return True

    def check_attr(self, attr, value):
        """Checks the class attributes and its value"""
        if attr == "":
            print("** attribute name missing **")
            return False
        elif value == "":
            print("** value missing **")
            return False
        return True

    def command_line(self, arg, num_args):
        """Fill 'line' list with user's arguments"""

        args = shlex.split(arg)
        line = []

        for i in range(num_args):
            if (len(args) > i):
                line.append(args[i])
                continue
            line.append("")

        return line


if __name__ == '__main__':
    HBNBCommand().cmdloop()
