#!/usr/bin/python3

"""this module contains tests for FileStorage class"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import unittest
import models


class Test_file_storage(unittest.TestCase):
    """tests instatntation for file_storage"""
    def test_instantation(self):
        fs = FileStorage()
        self.assertEqual(type(fs), FileStorage)

    def test_attr(self):
        fs = FileStorage()
        self.assertFalse(hasattr(fs, '__file_path'))

class Test_file_storage_methods(unittest.TestCase):
    """tests public instance methods for file_storage"""
    def test_all(self):
        all_objs = models.storage.all()
        self.assertEqual(type(all_objs), dict)
    def test_new(self):
        my_model = BaseModel()
        models.storage.new(my_model)
        self.assertIn('BaseModel.' + my_model.id, models.storage.all())
    def test_save(self):
        my_model = BaseModel()
        my_model.save()
        with open('file.json', 'r') as f:
            line = f.read()
            self.assertIn('BaseModel.' + my_model.id, line)
    def test_reload(self):
        my_model = BaseModel()
        models.storage.save()
        models.storage.reload()
        obj = FileStorage._FileStorage__objects
        self.assertIn('BaseModel.' + my_model.id, obj)

if __name__ == '__main__':
    unittest.main()