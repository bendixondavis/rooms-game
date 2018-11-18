class Room:
    def __init__(self,text,adjacent_rooms):
        self.text = text
        self.adjacent_rooms = adjacent_rooms

    def print_text(self):
        print(self.text)

    def get_adjacent(self):
        return self.adjacent_rooms
