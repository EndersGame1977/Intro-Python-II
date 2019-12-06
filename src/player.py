# Write a class to hold player information, e.g. what room they are in
# currently.

import sys


class Player():
    """ A player, their race and location """

    def __init__(self, name, age, current_room, item):
        self.name = name
        self.age = age
        self.current_room = current_room
        self.item = [item]

    def move(self, direction):
        if direction == 'n':
            self.current_room = self.current_room.n_to
        elif direction == 'e':
            self.current_room = self.current_room.e_to
        elif direction == 'w':
            self.current_room = self.current_room.w_to
        elif direction == 's':
            self.current_room = self.current_room.s_to
        elif direction == 'q':
            print("Thanks for playing")
            sys.exit()
        else:
            print()
            print("Please choose n, s, e, or w as direction.")

    def inventory(self, item):
        if item in self.item:
            self.item.remove(item)
            self.current_room.item.append(item)
        else:
            self.item.append(item)
            self.current_room.item.remove(item)
