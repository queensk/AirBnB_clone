#!/usr/bin/python3
"""
Defines the BaseModel class.
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Class defines all common attributes/methods for other classes:
    """

    def __init__(self, *args, **kwargs):
        """
        Base class initialization

        Args:
            args: unused.
            kwargs: (dict) Key/value pairs of attributes.
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    self.__dict__[k] = datetime.strptime(v, time_format)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """
        Save depending on the current date time.
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Returns Dictionary of the base model instance

        Includes the key value pairs __class__ representation
        of the class name of the object
        """
        rep_dict = self.__dict__.copy()
        rep_dict["created_at"] = self.created_at.isoformat()
        rep_dict["updated_at"] = self.created_at.isoformat()
        rep_dict["__class__"] = self.__class__.__name__
        return rep_dict

    def __str__(self):
        """
        Returns the print string representation of the base Model.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
