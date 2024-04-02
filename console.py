#!/usr/bin/python3
"""Console module containing the entry point of the command interpreter."""
import cmd


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

    def help_quit(self):
        """ Help message for quit command."""
        print("Quit the console.")

    def help_EOF(self):
        """Help message for EOF command."""
        print("Exit the console.")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
