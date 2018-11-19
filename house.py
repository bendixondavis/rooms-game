from room import Room
from graph import Graph

class House:
    def __init__(self,rooms,current_room):
        self.rooms = rooms
        self.current_room = current_room

    def get_current_room(self):
        return self.current_room.title

    def set_current_room(self,room):
        for e in self.rooms:
            if e.title == room.title:
                self.current_room = room

    #creates a graph to map out the house
    def init_house_graph(self):
        graph = Graph({})
        for room in self.rooms:    
            graph.add_node(room.title,room.get_adjacent())
        return graph
