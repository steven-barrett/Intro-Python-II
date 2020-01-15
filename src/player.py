# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room='outside', items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    def __str__(self):
        return f'Player {self.name} is in room {self.current_room}'

    def move(self, direction):
        self.current_room = getattr(self.current_room, f'{direction}_to')

    def inventory(self):
        if len(self.items) == 0:
            print('You have no items in your inventory')
        else:
            for item in self.items:
                print(item)
