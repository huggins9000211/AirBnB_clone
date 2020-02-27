#!/usr/bin/python3
""" File Storage """
import json
import models
import copy


class FileStorage():
    """ File Storage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ All """
        return self.__objects

    def new(self, obj):
        """ New """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ Save """
        newDict = {}
        for x, y in copy.deepcopy(self.__objects).items():
            newDict[x] = y.to_dict()
        data = json.dumps(newDict)
        with open(self.__file_path, 'w') as f:
            f.write(data)

    def reload(self):
        """ Reload """
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.review import Review
        newDict2 = {}
        try:
            with open(self.__file_path) as f:
                loadedString = f.read()
                newDict2 = json.loads(loadedString)
                for x, y in newDict2.items():
                    if x.split(".")[0] == "BaseModel":
                        newDict2[x] = BaseModel(**y)
                    elif x.split(".")[0] == "User":
                        newDict2[x] = User(**y)
                    elif x.split(".")[0] == "State":
                        newDict2[x] = State(**y)
                    elif x.split(".")[0] == "City":
                        newDict2[x] = City(**y)
                    elif x.split(".")[0] == "Amenity":
                        newDict2[x] = Amenity(**y)
                    elif x.split(".")[0] == "Place":
                        newDict2[x] = Place(**y)
                    elif x.split(".")[0] == "Review":
                        newDict2[x] = Review(**y)
                self.__objects = newDict2
        except FileNotFoundError:
            pass
