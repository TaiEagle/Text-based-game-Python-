#Tai Osborne
"""
This is the first project I created in college

"""
rooms = {
    "Main office": {"North": "Financial analyst office", "East": "Analyst office", "South":"Targeter office", "West":"Boss’s office"},
    "Financial analyst office": {"East": "Home location analyst office", "South": "Main office"},
    "Home location analyst office": {"West": "Financial analyst office"},
    "Boss’s office": {"East": "Main office"},
    "Targeter office": {"North": "Main office", "East": "I.T. office"},
    "I.T. office": {"West": "Targeter office"},
    "Analyst office": {"North": "Basement", "West": "Main office"},
    "Basement": {"South": "Analyst office"}
}
items ={
    "Financial analyst office": "finances of target",
    "Home location analyst office": "location of target’s home",
    "Boss’s office": "boss’s permission",
    "Targeter office": "information about target",
    "I.T. office": "live location of target’s phone",
    "Analyst office": "proof of national security risk",
    "Main office": "There is nothing in this room"
}
current_room = "Main office"
inventory = []
current_option = ''
initiator = 0
game_loop = 0
#move between rooms
def move():
    global current_room, current_option, game_loop
    print('\nYou can travel these directions: ' , end="")
    for i in rooms[current_room].keys():
        print(i, "", end="")
    print()
    direction = input("\nEnter your direction: ")
    while direction not in rooms[current_room]:
        direction = input("Enter a valid direction to move: ")
    if direction in rooms[current_room]:
        current_room = rooms[current_room][direction]
    if current_room == "Basement" and len(inventory) == 6:
        print("\nYou won! You have met the monster in the basement. The target has been eliminated.")
        game_loop = 1
    elif current_room == "Basement" and len(inventory) < 6:
        print("\nYou lost! You met the monster in the basement without all of the necessary items. The target got away.")
        game_loop = 1
#user options
def options():
    global current_option, initiator
    print('-' * 56)
    if current_room == "Main office":
        print('You are in the {}\n'.format(current_room))
        retrieve("print_inventory")
        current_option = input("Say 'move' to move to the next room: ")
        if current_option == "move":
            pass
        else:
            while True:
                current_option = input("Enter a valid option. Say 'move' to move to the next room: ")
                if current_option == 'move':
                    break
    else:
        print('You are in the {}\n'.format(current_room))
        retrieve("print_inventory")
        current_option = input("Say 'move' to move to the next room, or 'pick up' to add items to your inventory: ")
        if current_option == 'pick up' or current_option == 'move':
            pass
        else:
            while True:
                current_option = input("Enter a valid option. Say 'move' to move to the next room or 'pick up' to add items to your inventory: ")
                if current_option == 'pick up' or current_option == 'move':
                    break
#function to retrieve the item
def retrieve(conditional):
    global current_room, current_option
    if conditional == "print_inventory":
        print("Items in this room: {}\n".format(items[current_room]))
        if len(inventory) > 0:
            print("Items in your inventory: ", end="")
            for index, value in enumerate(inventory):
                if index < len(inventory) -1:
                    print(value, ', ', end="")
                else:
                    print(value)
                    print()
    if conditional == "add_to_inventory":
        if items[current_room] in inventory:
            print("You already have this item in your inventory\n")
        else:
            inventory.append(items[current_room])
#game loop
def game():
    global current_option, current_room
    while game_loop == 0:
        options()
        if current_option == 'pick up':
            retrieve("add_to_inventory")
        if current_option == 'move':
            move()
game()