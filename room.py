class Room:
    def __init__(self,title,text,adjacent_rooms):
        self.title = title
        self.text = text
        self.adjacent_rooms = adjacent_rooms

    def print_text(self):
        print(self.text)

    def get_title(self):
        return self.title

    def get_adjacent(self):
        return self.adjacent_rooms
