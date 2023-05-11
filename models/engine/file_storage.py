#!/usr/bin/python3

"""
    serializes instances to a JSON file
    deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
        declare the private attributes
        __file_path(str) - path to json file
        __objects(dict) - store all objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        obj_key = type(obj).__name__ + "." + obj.id
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_file = FileStorage.__file_path
        json_str = ""
        new_dict = {}

        for k, v in FileStorage.__objects.items():
            new_dict[k] = v.to_dict()
        with open(json_file, mode="w") as f:
            json_str = json.dumps(new_dict)
            f.write(json_str)

    def reload(self):
        """deserializes the JSON file to __objects"""
        json_file = FileStorage.__file_path

        try:
            with open(json_file, mode="r") as f:
                json_str = f.read()
                new_dict = json.loads(json_str)

                for k, v in new_dict.items():
                    if 'BaseModel' in k:
                        new_dict[k] = BaseModel(**v)
        except FileNotFoundError:
            pass
