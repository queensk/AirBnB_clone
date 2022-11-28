#!/usr/bin/python3
"""
Module defines city class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class representation

    Attributes:
        state_id: The state id (str).
        name: The state name (str).
    """

    state_id = ""
    name = ""
