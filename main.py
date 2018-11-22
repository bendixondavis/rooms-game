from player import Player
from room import Room
from house import House

def get_story_item(text,tag):
    #this method is given a string and a tag, it searches for the tag
    #and returns all text following that tag until it reachs a [
    #this is meant to search text in a file that is in ini style where section headers are inside [] brackets
    #but instead of key pairs what is in each section is just a block of text

    index = text.find(tag) + len(tag) #finds the tag searched for and returns index of the first character past the tag
    end_index = text.find("[" , index + len(tag)) #finds the index of where the first [ is after the tag
    item = text[index:end_index] #gets the text after the tag
    return item

def init_rooms():
    #initialize all rooms with their text description and adjacent rooms
    #adjacent rooms in format of [forward,backward,right,left,up,down]
    #use blank string to show that you can't move in that direction
    #returns list of all rooms
    entry = Room('entry',get_story_item(story,"[Entry]"),
            ["closet",'',"bedroom","kitchen",'',''])
    closet = Room('closet',get_story_item(story,"[Closet]"),
            ['',"entry",'','','',''])
    bathroom = Room('bathroom',get_story_item(story,"[Bathroom]"),
            ['',"bedroom",'','','',''])
    kitchen = Room('kitchen',get_story_item(story,"[Kitchen]"),
            ['',"entry",'','','',''])
    bedroom = Room('bedroom',get_story_item(story,"[Bedroom]"),
            ['',"entry","bathroom",'','',''])
    rooms = [entry,closet,bathroom,kitchen,bedroom]
    return rooms

def intro(player):
    print(intro_text.format(player))

def get_player_name():
    player_name = input("Hello, what is your name? ")
    return player_name

def get_direction():
    pick = input("Do you want to go Forward(F), Backward(B), "
                "Right(R), Left(L), Up(U), Down(D) or Quit(Q)?")
    return pick

def get_rooms_connect(graph,key):
    connections = graph.get(key)
    return connections

def main():
    player = Player(get_player_name())   #get input for player name
    intro(player.first_name)   #format player name into intro text
    rooms = init_rooms()
    house = House(rooms,rooms[0])
    map = house.init_house_graph()

    #state machine loop
    while True:
        room_in = house.get_current_room()
        room_in.print_text()
        choice = get_direction()
        next_rooms = room_in.get_adjacent()

        #these if statements index the list of adjacent rooms to move to next room
        if choice == 'F':
            if next_rooms[0] != '':
                print(next_rooms[0])
                house.set_current_room(next_rooms[0])
            else:
                print("can't go that way...")
        if choice == 'B':
            if next_rooms[1] != '':
                house.set_current_room(next_rooms[1])
            else:
                print("can't go that way...")
        if choice == 'R':
            if next_rooms[2] != '':
                house.set_current_room(next_rooms[2])
            else:
                print("can't go that way...")
        if choice == 'L':
            if next_rooms[3] != '':
                house.set_current_room(next_rooms[3])
            else:
                print("can't go that way...")
        if choice == 'U':
            if next_rooms[4] != '':
                house.set_current_room(next_rooms[4])
            else:
                print("can't go that way...")
        if choice == 'D':
            if next_rooms[5] != '':
                house.set_current_room(next_rooms[5])
            else:
                print("can't go that way...")
        if choice == 'Q':
            break

bin_file = open("rooms.bin","rb")   #opens bin file that contains all of the story text
story = bin_file.read().decode()    #reads the contents of the file into a string

#initialize text description for the game intro
intro_text = get_story_item(story,"[Intro]")

if __name__=="__main__":
    main()
