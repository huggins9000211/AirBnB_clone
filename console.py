#!/usr/bin/python3
"""Console for AirBnB project"""
import cmd
import models
import shlex
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter"""
    prompt = "(hbnb) "
    storage = models.storage
    myClasses = [
        "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def do_quit(self, line):
        """Quits the program"""
        return True

    def emptyline(self):
        """Does nothing if the user presses ENTER"""
        pass

    def do_EOF(self, line):
        """Quits the program at end of the file"""
        print('')
        return True

    def do_create(self, line):
        """ create [class] - Creates new object """
        argss = shlex.split(line)
        if line == "":
            print("** class name missing **")
        elif argss[0] == "BaseModel":
            new = BaseModel()
            self.storage.save()
            print(new.id)
        elif argss[0] == "User":
            new = User()
            self.storage.save()
            print(new.id)
        elif argss[0] == "State":
            new = State()
            self.storage.save()
            print(new.id)
        elif argss[0] == "City":
            new = City()
            self.storage.save()
            print(new.id)
        elif argss[0] == "Amenity":
            new = Amenity()
            self.storage.save()
            print(new.id)
        elif argss[0] == "Place":
            new = Place()
            self.storage.save()
            print(new.id)
        elif argss[0] == "Review":
            new = Review()
            self.storage.save()
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """ show [class name] [id] - Shows object """
        argss = shlex.split(line)
        if len(argss) == 0:
            print("** class name missing **")
        elif argss[0] in self.myClasses:
            if len(argss) == 1:
                print("** instance id missing **")
                return
            allObj = self.storage.all()
            for x, y in allObj.items():
                if x == "{}.{}".format(argss[0], argss[1]):
                    print(y)
                    return
            print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """ destroy [class name] [id] - Destroys object """
        argss = shlex.split(line)
        if len(argss) == 0:
            print("** class name missing **")
        elif argss[0] in self.myClasses:
            if len(argss) == 1:
                print("** instance id missing **")
                return
            allObj = self.storage.all()
            for x, y in allObj.items():
                if x == "{}.{}".format(argss[0], argss[1]):
                    del allObj[x]
                    self.storage.save()
                    return
            print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        """ all [class name] - Shows all objects class name optional """
        argss = shlex.split(line)
        allObj = self.storage.all()
        result = []
        if len(argss) == 0:
            for x, y in allObj.items():
                result.append(str(y))
            print(result)
        else:
            if not argss[0] in self.myClasses:
                print("** class doesn't exist **")
                return
            for x, y in allObj.items():
                if(x.split('.')[0] == argss[0]):
                    result.append(str(y))
            print(result)

    def do_update(self, line):
        """ update [class name] [id] [attribute name] "[attribute value]"
        - Updates object """
        argss = shlex.split(line)
        if len(argss) == 0:
            print("** class name missing **")
        elif argss[0] in self.myClasses:
            if len(argss) == 1:
                print("** instance id missing **")
                return
            allObj = self.storage.all()
            for x, y in allObj.items():
                if x == "{}.{}".format(argss[0], argss[1]):
                    if len(argss) == 2:
                        print("** attribute name missing **")
                        return
                    if len(argss) == 3:
                        print("** value missing **")
                        return
                    try:
                        myType = type(getattr(y, argss[2]))
                    except:
                        setattr(y, argss[2], argss[3])
                    else:
                        setattr(y, argss[2], myType(argss[3]))
                    y.save()
                    return
            print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def default(self, line):
        """ Overide default """
        allObj = self.storage.all()
        try:
            customCommand = line.split('.')[1].split('(')[0]
            if customCommand == "all":
                myList = []
                for x, y in allObj.items():
                    if x.split('.')[0] == line.split('.')[0]:
                        myList.append(str(y))
                        print(("[{}]".format(
                            ', '.join(map(str, myList)))))
            elif customCommand == "count":
                count = 0
                for x, y in allObj.items():
                    if x.split('.')[0] == line.split('.')[0]:
                        count += 1
                print(count)
            elif customCommand == "show":
                self.do_show(line.split('.')[0] + ' ' + line.split(
                    '.')[1].split('(')[1][:-1].strip('" '))
            elif customCommand == "destroy":
                self.do_destroy(line.split('.')[0] + ' ' + line.split(
                    '.')[1].split('(')[1][:-1].strip('" '))
            elif customCommand == "update":
                myArgs = line.split('(')[1][:-1]
                if '{' in line:
                    className = line.split('.')[0]
                    id = myArgs[:myArgs.find(',')]
                    myDict = line.split('{')[1][:-1]
                    myDict = myDict.split(', ')
                    for x in myDict:
                        self.do_update(
                            className + " " + id + " " + x.split(
                                ": ")[0] + " " + x.split(": ")[1])
                else:
                    self.do_update(line.split(
                        '.')[0] + ' ' + line.split(
                        '.')[1].split('(')[1][:-1].strip(' ').replace(',', ''))
            else:
                return super().default(line)
        except IndexError:
            return super().default(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
