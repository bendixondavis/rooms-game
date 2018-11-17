from player import Player

def get_story_item(text,tag):
    #this method is given a string and a tag, it searches for the tag
    #and returns all text following that tag until it reachs a [
    #this is meant to search text in a file that is in ini style where section headers are inside [] brackets
    #but instead of key pairs what is in each section is just a block of text

    index = text.find(tag) + len(tag) #finds the tag searched for and returns index of the first character past the tag
    end_index = text.find("[" , index + len(tag)) #finds the index of where the first [ is after the tag
    item = text[index:end_index] #gets the text after the tag
    return item

def intro(player):
    print(intro_text.format(player))

def get_player_name():
    player_name = input("Hello, what is your name? ")
    return player_name

def get_direction():
    pick = input("Do you want to go Right(R), Left(L), Forward(F), Backward(B) or Run(R)?")
    return pick

def get_rooms_connect(graph,key):
    connections = graph.get(key)
    return connections

def main():
    player = Player(get_player_name())   #get input for player name
    intro(player.first_name)   #format player name into intro text
    print(entry_text)    #output entryway text
    choice = get_direction()
    while choice != "R":
        print(choice)
        choice = get_direction()
        print(get_rooms_connect(house,"entry"))

# 0 in map represents haven't been to that room,
# 1 repesents have been to it, X repesents current room
map = [0,0,0]

bin_file = open("rooms.bin","rb")   #opens bin file that contains all of the story text
story = bin_file.read().decode()    #reads the contents of the file into a string

#initialize all of the text descriptions for the game intro and all rooms
intro_text = get_story_item(story,"[Intro]")
entry_text = get_story_item(story,"[Entry]")
closet_text = get_story_item(story,"[Closet]")
bathroom_text = get_story_item(story,"[Bathroom]")
kitchen_text = get_story_item(story,"[Kitchen]")
bedroom_text = get_story_item(story,"[Bedroom]")
house = {"entry":["closet","bedroom","kitchen"],
        "closet":["entry"],
        "bathroom":["bedroom"],
        "kitchen":["entry"],
        "bedroom":["entry","bathroom"]}

if __name__=="__main__":
    main()
