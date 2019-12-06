from room import Room
from player import Player
from item import Item

# itmes

item = {
    "compass": Item("compass", "This should show you the way"),
    "pencil": Item("pencil", "Ordinary pencil?"),
    "rock": Item("rock", "Could come in handy..."),
    "gun": Item("gun", "Keep this at arms reach!"),
    "hammer": Item("hammer", "Keep this at arms reach!"),
    "money": Item("money", "Don't waste time counting"),
    "telescope": Item("telescope", "Can you see anything nice?"),
    "gold": Item("gold", "Is it real?"),
    "crowbar": Item("crowbar", "Do you have a use for this?"),
    "donut": Item("donut", "A little pick me up"),
    "shakles": Item("shakles", "From escapes prisoners"),
    "teeth": Item("teeth", "Teeth on the floor... gross"),
    "flares": Item("flares", "Still have that gun?"),
    "ladder": Item("ladder", "Is it long enough "),
    "rope": Item("rope", "Maybe its long enough to get down?")
}

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", None),
    'foyer':    Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east.", None),
    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.", None),
    'narrow':   Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air.", None),
    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.", None),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add items to rooms

room['foyer'].item = [item['rock'], item['gun']]
room['overlook'].item = [item['hammer'], item['money']]
room['narrow'].item = [item['telescope'], item['gold']]
room['treasure'].item = [item['crowbar'], item['donut']]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


current_player = Player("Jason", 42, room['outside'], None)


print()
print("Your current location is", current_player.current_room.name)
print("You have these items: ", current_player.item)
print("The items at this location are: ", current_player.current_room.item)
print(current_player.current_room.description)
print()

while True:
    direction = input('Please choose a direction: ')
    if direction.lower():
        current_player.move(direction)
        print()
        print("You are in a ", current_player.current_room.name)
        print("You have these items: ", current_player.item)
        print("The items at this location are: ",
              current_player.current_room.item)
        print(current_player.current_room.description)
        print()
        stuff = input("Type the name of the item to add or remove item: ")
        for i in current_player.current_room.item:
            if str(i) == stuff:
                current_player.current_room.item.remove(i)
                current_player.item.append(i)
                print("You picked up a", i)
            else:
                current_player.current_room.item.append(i)
                current_player.item.remove(i)
                print("You dropped ", i)
