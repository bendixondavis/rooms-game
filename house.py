from room import Room

class House:
    def __init__(self,rooms,current_room):
        self.rooms = rooms
        self.current_room = current_room

    def get_next_room(self,choice):
        adjacent_rooms = self.current_room.get_adjacent()

room = [Room('Hello there',[['basement'],['F']])]
house = House(room,'entry')

print(house.rooms[0])
print(house.current_room)
