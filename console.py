#!/usr/bin/python3
""""
    This module contains the Console
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """A console class were all the console function it works"""
    prompt = '(hbnb) '
    classesList = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review",
    ]
    

    def do_quit(self, arg):
        """ to exit the program"""
        return True

    def do_EOF(self, arg):
        """ to exit the program"""
        return True

    def emptyline(self):
        """avoids an empty line when using enter"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id."""
        splitedARG = arg.split()
        if len(arg) < 1:
            print("** class name missing **")
        elif splitedARG[0] == "BaseModel":
            newBaseModel = BaseModel()
            newBaseModel.save()
            print(newBaseModel.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the
        class name and id."""
        splitedARG = arg.split()
        if len(splitedARG) < 1:
            print("** class name missing **")
        elif len(splitedARG) < 2:
            print("** instance id missing **")
        else:
            if splitedARG[0] not in self.classesList:
                print("** class doesn't exist **")
            else:
                class_and_id = splitedARG[0] + '.' + splitedARG[1]
                objects = storage.all()
                if class_and_id in objects:
                    print(objects[class_and_id])
                else: print("** no instance found **")
        


    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the
        change into the JSON file)."""
        splitedARG = arg.split()
        if len(splitedARG) < 1:
            print("** class name missing **")
        elif len(splitedARG) < 2:
            print("** instance id missing **")
        else:
            if splitedARG[0] not in self.classesList:
                print("** class doesn't exist **")
            else:
                class_and_id = splitedARG[0] + '.' + splitedARG[1]
                objects = storage.all()
                if class_and_id in objects:
                    del objects[class_and_id]
                    storage.save()
                else: print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or
        not on the class name."""
        splitedARG = arg.split()
        my_list = []
        objects = storage.all()
        if not arg:
            for obj in objects:
                my_list.append(str(objects[obj]))
                print(my_list)
        else:
            if splitedARG[0] in self.classesList:
                for obj in objects:
                    if obj.split('.')[0] == splitedARG[0]:
                        my_list.append(str(objects[obj]))
                print(my_list)
            else:
                 print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)."""
        splitedARG = arg.split()
        if len(splitedARG) < 1:
            print("** class name missing **")
        elif len(splitedARG) < 2:
            print("** instance id missing **")
        elif len(splitedARG) < 3:
            print("** value missing **")
        else:
            class_Name = arg[0]
            idValue = eval(arg[1])
            prop = eval(arg[2])
            value = arg[3]

            if splitedARG[0] not in self.classesList:
                print("** class doesn't exist **")
            else:
                class_and_id = splitedARG[0] + '.' + splitedARG[1]
                objects = storage.all()
                if class_and_id in objects:
                    for obj in objects:
                        if obj.idValue == arg[1]:
                            obj.prop == value

                else: print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()