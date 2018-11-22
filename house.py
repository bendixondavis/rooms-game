from room import Room

class House:
    def __init__(self,rooms,current_room):
        self.rooms = rooms
        self.current_room = current_room

    def get_current_room(self):
        return self.current_room

    def set_current_room(self,room_title):
        for e in self.rooms:
            if e.title == room_title:
                self.current_room = e
