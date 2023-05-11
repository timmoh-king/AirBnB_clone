#!/usr/bin/python3

"""
class BaseModel that defines all common attributes/methods for other classes
"""
from datetime import datetime
import uuid


class BaseModel:
    """defines all common attributes/methods for other classes
        Declare the public instances:
        Id (string): assign with an uuid
        created_at (datetime): the curr datetime when an inst is created
        updated_at (datetime): the curr datetime when an inst is updated
    """
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __str__(self):
        """should print [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the public inst attr updated_at with the curr datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dict containing all key/val of __dict__ of the inst"""
        new_dict = {'__class__': type(self).__name__,
                    'updated_at': self.updated_at.isoformat(), 'id': self.id,
                    'created_at': self.created_at.isoformat()}
        new_dict.update(**self.__dict__)
        return new_dict
