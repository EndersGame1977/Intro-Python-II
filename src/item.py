
class Item():
    """Items that are in the rooms and player can carry"""

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return self.name
