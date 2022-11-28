#!/usr/bin/python3
"""
Defines the FileStorage class.
"""
import json


class FileStorage:
    """
    Represents an abstract file storage engin.

    Attribute:
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary - empty but will store all objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary object.
        """
        return FileStorage._objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        object_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(object_class_name, obj.id)] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        o_dict = FileStorage.__objects
        obj_dict = {obj: o_dict[obj].to_dict() for obj in o_dict.keys()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserialize the JSON file __file_path to __objects, if it exists.
        """
        try:
            with open(FileStorage.__file_path) as f:
                object = json.load(f)
                for o in object.values():
                    class_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(class_name)(**o))
        except FileNotFoundError:
            return
