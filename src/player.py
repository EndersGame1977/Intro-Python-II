# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    """ A player, their race and location """

    def __init__(self, name, age, current_room):
        self.name = name
        self.age = age
        self.current_room = current_room
