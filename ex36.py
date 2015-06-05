from sys import exit

# Here is where the adventure starts.
def start():
    print "You wake up in a dark room."
    print "You don't know how you got here."
    print "There is a door on each side of the room."
    print "Good news is each door is labled with a "
    print "direction like north, west south and east." 
    print "Bad news is you don't know what's behind each door."
    print "So which door to go through first?"
    print "'North', 'West', 'South', 'East', or something else?"
    
    choice = raw_input("> ")
    
    if choice == "north":
        north_room()
    if choice == "west":
        west_room()
    if choice == "south":
        south_room()
    if choice == "east":
        east_room()
    else:
        dead("Well whatever you tried, since that did not work, you wound up starving to death.")

# this is for when you come back to the start agian.
def start2():
    print "So you make your back to this dreary room..."
    print "which way do you want to go?"
    print "'North', 'West', 'South', 'East', or try something else?"
    
    choice = raw_input("> ")
    
    if choice == "north":
        north_room()
    if choice == "west":
        west_room()
    if choice == "south":
        south_room()
    if choice == "east":
        east_room()
    else:
        dead("Well you tried whatever that something was, and since that did not work, you wound up starving to death.")

# this takes care of all the death notes.    
def dead(why):
    print why, "Better luck in the next life..."
    exit(0)
    
# This is what happens in the north room
def north_room():
    print "You decided to go through the north room"
    print "Upon entering the north room you see a box in the middle"
    print "You dont see much else..."
    print "Do you want to 'open' the box, 'leave' the room, or try anything else?"
    
    choice = raw_input("> ")
    
    if "open" in choice:
        dead("As you pear inside, a tentacle grabs hold of you and drags you in.")
    elif "leave" in choice:
        start2()
    else:
        print "Well whatever you just tried, it did not work or do anything."
        north_room()

# this is what happens in the the west room.
def west_room():
    print "You decide to go through the west door"
    print "You see a statue in the middle of the room."
    print "It's a statue of a knight with a long sword."
    print "You also see another door behind the statue."
    print "There is also something written on the base of the statue."
    print "what do you plan to do? 'open' door, 'read', 'touch' the statue, or 'leave'?"
    
    choice = raw_input("> ")
    
    if "touch" in choice:
        dead("The knight comes to life and chops you in half.")
    elif "open" in choice:
        dead("The knight comes to life and chops your head off.")
    elif "read" in choice:
        print "It reads 'Thou shall not pass! upon death by beheading'"
        west_room()
    elif "leave" in choice:
        start2()
    else:
        print "Well whatever you just tried, it did not work or do anything."
        west_room()

# This is what happens in the south door.     
def south_room():
    print "You go through the south door."
    print "You find three doors in this room and not much else."
    print "what do you want to do?"
    print "go through the 'left' door, the 'middle' door, the 'right' door or just 'leave'?"
    
    choice = raw_input("> ")
    
    if "left" in choice:
        dead("As you go for the left door, it opens and a giant hand grabs and crushes you.")
    elif "middle" in choice:
        dead("As you go for the middle door, the floor crumbles and you fall into the darkness, never to be heard from again.")
    elif "right" in choice:
        dead("As you go for the right door, a 'click' sounds and arrow appears in your chest.")
    elif "leave" in choice:
        start2()
    else:
        print "Well whatever you just tried, it did not work or do anything."
        south_room()

# this is what happens in the east room
def east_room():
    print "You go through the east door."
    print "You find two doors and sign post."
    print "What do you do now?"
    print "go through the 'left' door? the 'right' door or 'read' the sign post?."
    
    choice = raw_input("> ")
    
    if "left" in choice:
        dead("You enter into the darkness, walk for days then starve never reaching the end.")
    elif "right" in choice:
        new_room()
    elif "read" in choice:
        print "It reads 'Make sure you are going the right way'."
        east_room()
    else:
        print "Well whatever you just tried, it did not work or do anything."
        east_room()
        
# this is what happens in the new room
def new_room():
    print "You entered through the right door."
    print "You see a sleeping bear in front of a door."
    print "On the left you see jars filled with honey."
    print "On the right you see a empty bowl and a pull rope"
    print "What do you plan to do?"
    print "Are you going to 'poke bear'?"
    print "How about 'fill bowl' or 'pull rope' just to see what happens?"
    print "You can also 'leave' and go back to the last room."

    bear_sleep = True
    bowl_filled = False
    
    while True:
        choice = raw_input("> ")
        
        if choice == ("poke bear" or "wake bear") and bear_sleep:
            dead("The bear wakes up mad and proceeds to eat you.")
        elif choice == "pull rope" and (bowl_filled == False):
            dead("A gong rings, the bear wakes up, comes to the bowl and see nothing, gets mad and eats you.")
        elif choice == "fill bowl":
            print "You fill the bowl with honey."
            bowl_filled = True
        elif choice == "pull rope" and (bowl_filled == True):
            print "A gong rings, the bear wakes up and comes over to eat from the" 
            print "bowl. The door is not blocked anymore you can 'open' it."
            bear_sleep = False
        elif "open" in choice and (bear_sleep == False):
            last_room()
        elif choice == "leave":
            east_room()
        else:
            print "That action makes you look silly."
        
# This is what happens in the last room.
def last_room():
    print "You go through the door with out anymore trouble."
    print "You see a staircase and at the top you can see sunlight."
    print "You also see a shiny treasure chest on the left."
    print "What do you plan to do?"
    print "Go and 'open' the chest or 'go' up the stairs?"
    
    while True:
        choice = raw_input("> ")
    
        if ("go" or "up") in choice:
            print "You had enough of this place and you go up the stairs."
            print "Congrats you made it out and you make it home."
            print "You win!"
            exit(0)
        elif "open" in choice:
            dead("As soon as you open the chest, a tentacle grabs you and pulls you into the box, and the lid slams shut.")
        else:
            print "That action makes you look silly."   
    
        
start()
