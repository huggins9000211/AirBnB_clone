#!/usr/bin/python3
""" Base Model """
import uuid
import copy
from datetime import datetime
import models


class BaseModel():
    """ Base """

    def __init__(self, *args, **kwargs):
        """ Init """
        if kwargs:
            try:
                for x, y in kwargs.items():
                    if x == "__class__":
                        continue
                    if x == "created_at" or x == "updated_at":
                        y = datetime.strptime(y, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, x, y)
            except TypeError:
                pass
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """ Str """
        return("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ Save """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ to Dict """
        mydict = copy.deepcopy(self.__dict__)
        mydict["__class__"] = self.__class__.__name__
        mydict["created_at"] = mydict["created_at"].isoformat()
        mydict["updated_at"] = mydict["updated_at"].isoformat()
        return mydict
