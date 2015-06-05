print "You enter a dark room with two doors. Do you go throught door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. what do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    print "3. Make your self look big by raising your arms."
    print "4. Back away slowly."
    print "5. Sneak around the bear."
    print "6. Stare at the bear."
    print "7. pretend to be a bear."
    print "8. Jump kick the bear."
    print "9. Offer to make tea."

    bear = raw_input("> ")
    
    if bear == "1":
        print "The bear eat's your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    elif bear == "3":
        print "The bear gets up and shows you its bigger and proceeeds to eat you. Good job!"
    elif bear == "4":
        print "The bear starts to chase you and eats you. Good job!"
    elif bear == "5":
        print "The bear does not notice you till you bump into a rock, then eats you. Good job!"
    elif bear == "6":
        print "The bear stares back at you, when you move you get eaten. Good job!"
    elif bear == "7":
        print "The bear takes offence and eats you. Good job!"
    elif bear == "8":
        print "The bear gets angry that you jumped kicked him, then eats eats you. Good job!"
    elif bear == "9":
        print "The bear says 'thanks, come have a seat and eat with me'. Good job!"
    else:
        print "Well doing %s is probally better. Bear runs away." % bear
        

elif door =="2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."
    print "4. Flashing stars and exploding yellow lights"
    print "5. Money raining upwards, cars flying in."
    print "6. Diamonds, gold, rubies, cool aid."
    print "7. Ocean of roaches, and swarms of flies."
    print "8. Flood of rats, hordes of bugs."
    print "9. Re-living your life up to this point again, and again."
    
    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    elif insanity == "3" or insanity == "4":
        print "Your mind snaps and you drop dead."
    elif insanity == "5" or insanity == "6":
        print "You seeing the bills, and bills or bills, you scream your throat raw and die."
    elif insanity == "7" or insanity == "8":
        print "You start to swat at imaginary pest and beat yourself silly."
    else:
        print "The insanity rots yours eyes into a pool of muck. Good job!"
        
else:
    print "You stumble around and fall on a knife and die. Good job!"
