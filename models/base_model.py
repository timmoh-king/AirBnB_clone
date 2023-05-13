#!/usr/bin/python3

"""
class BaseModel that defines all common attributes/methods for other classes
"""
from datetime import datetime
import uuid


class BaseModel:
    """defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        from models import storage
        """
            Declare the public instances:
            Id (string): assign with an uuid
            created_at (datetime): the curr datetime when an inst is created
            updated_at (datetime): the curr datetime when an inst is updated
        """
        date_form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, date_form)
                else:
                    self.__dict__[k] = v
        else:
            storage.new(self)

    def __str__(self):
        """should print [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        from models import storage
        """updates the public inst attr updated_at with the curr datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dict containing all key/val of __dict__ of the inst"""
        new_dict = self.__dict__.copy()
        new_dict['id'] = self.id
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['__class__'] = type(self).__name__
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
