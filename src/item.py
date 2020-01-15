class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'Item name: {self.name}'

    def on_take(self):
        print(f'"You picked up {self.name}"')

    def on_drop(self):
        print(f'You dropped {self.name}')
