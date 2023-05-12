#!/usr/bin/python3

"""a class User that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """
        declare the public attributes
        Args:
            email(str) - empty string
            password(str) - empty string
            first_name(str) - empty string
            last_name(str) - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
