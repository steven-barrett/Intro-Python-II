# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        return f'Room name: {self.name}. description: {self.description}'
# class Room:
#     def __init__(self, name, desc):
#         self.name = name
#         self.desc = desc        
#         self.n_to = None
#         self.s_to = None
#         self.e_to = None
#         self.w_to = None

#     def __repr__(self):
#         room = f"(Room({repr(self.name)}, {repr(self.description)}))"
#         return room

#     def __str__(self):
#         s = f"Room({self.name})"
#         return s

#     def description(self):
#         desc = f"{self.description}"
#         return desc

#     def getName(self):
#         name = f"{self.name}"
#         return name
