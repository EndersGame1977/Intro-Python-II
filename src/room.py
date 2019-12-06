# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item


class Room():
    """A room with a description"""

    def __init__(self, name, description, item):
        self.name = name
        self.description = description
        self.item = []
