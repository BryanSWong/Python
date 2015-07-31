print "It's the final match of the world fighters tournament."
print "Your opponent is Mark 'King of kick' James."
print "do you '1' strike first or '2' defend and counter?"

action1 = raw_input("Enter action: ")
print

if action1 == "1":
    print "Strike first is the way to go! whats your plan of attack?"
    print "1. Deliver the 'Ultimate Punch!' it has not failed you yet!"
    print "2. Beat the 'King of Kick' at his own game! Using 'Super Kick'."
    
    strike = raw_input("which attack to use? ")
    
    if strike == "1":
        print "Your 'Ultimate Punch' blows Mark James out of the ring! You win!"
        print
    elif strike == "2":
        print "Your 'Super Kick' does not match up to Mark James 'King Kick'! You lose as you fly out of the ring!"
        print
    else:
        print "What ever you tried fails as Mark Kicks you out of the ring. You lose"
        print
        
elif action1 == "2":
    print "Defend and counter is safer. How do you do it?"
    print "1. 'King of Kick' must be false title. get read to block a punch and counter with 'Ultimate punch'."
    print "2. Side step Mark James 'King Kick', then counter with 'Ultimate Punch'!"
    
    defend = raw_input("How to counter? ")
    print
    
    if defend == "1":
        print "Mark 'King of Kick' James was true to his title. He dilivers his 'King Kick and sends you flying. You lose! "
        print
    elif defend == "2":
        print "You side step like a pro, and your 'Ultimate Punch' send Mark flying. You Win!"
        print
    else:
        print "You never saw the 'King Kick' but you remmber flying out of the ring. You lose!"
        print

else:
    print "You took too long or decided something dumb, and Mark Kicks you in the head knocks you out cold, winning the tournament. You cry about it later."
    print   
