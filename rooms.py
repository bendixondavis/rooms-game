import random

# 0 in map represents haven't been to that room,
# 1 repesents have been to it, X repesents current room
map = [[0,0],[0,0]]

intro_text = ("You walk up to the old house at the end of the street. \n"
    "The paint is chipped and falling off.  \nThe gutters are hanging "
    "from the roof.  \nThe shingles are curled and falling off.  \n"
    "Most of the windows are broken and filled in with cobwebs. \n"
    "You decide to walk up to the door and knock.  \nThe door swings open "
    "and you hear a low whispered voice say '{}, please come in'.  ")
room1 = ("This room has a worn out, slumped bed.  "
        "Next to the bed is a dresser made of old worn wood with a cracked mirror.")
room2 = ("There is nothing of interest in this room.")
room3 = ("This is a kitchen.  The stove is rusted and covered in old grease."
        "There are pots and pans laying all over the floor.")
room4 = ("This is a bathroom.  The toilet bowl is filled with brown slime "
        "and the bathtub is stained and chipped.")
house = [room1, room2, room3, room4]
player = ""

def main():
    player = get_player()
    intro(player)
    #pick_room()

def intro(player):
    print(intro_text.format(player))

def get_player():
    player = input("Hello, what is your name? ")
    return player

def pick_room():
    print(house[random.randint(1,4)])

def check_map(map):
    print(map)

def update_map(map,room):

if __name__=="__main__":
    main()
