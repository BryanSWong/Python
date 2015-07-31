print """
map 

start "wake up in a dark room with four doors, on in each of the directions north south west and east.

choices are:
north door
east door
south door
west door
die of starvation if none of the doors are chosen


north
box_room() leads to death if box is opened
return to start

south
trap_room()
three doors all death traps
retun to start

west
Statue() leads to death when you mess with it.
return to start

east
two_doors() one leads to death other continues on.
return to start


two_doors() 
left death
right new_room()

new_room()

 you see a sleeping bear in front of a door, jars of honey on the right side, and on the left side is a empty bowl and a pull rope.
 
 poke the bear death
 pull rope and bowl empty death
 wake the bear death
 pour honey into bowl
 pull rope and bowl full bear wakes up and goes to bowl of honey to eat
 poke bear and bowl full death
 go through the door
 
 last_room()
 stairs going up leads to freedom and game win ending.
 huge treasure chest trap leads to trap door death
 
"""
