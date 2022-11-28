#!/usr/bin/python3
"""
User class definition
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Representation of a user.
    Attributes:
        email: Users email (str)
        password: Users password (str)
        first_name: Users first name (str)
        last_name: Users last name (str)
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
