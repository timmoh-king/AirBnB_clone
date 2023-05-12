#!/usr/bin/python3

"""classes that inherit from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """
        Declare the public class attributes
        Args
            name(str) - empty str
    """
    name = ""
