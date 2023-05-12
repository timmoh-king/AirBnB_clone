#!/usr/bin/python3

"""classes that inherit from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
        declare public class attributes
        name: string - empty string
    """
    name = ""
