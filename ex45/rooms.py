from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Bar(Scene):

    def enter(self):
        print " "
        print "You are the town 'Sherif' and is having a nice drink at the bar,"
        print "when your deputy runs into the bar and yells 'Sherif!' You start"
        print "to wonder what going on as your deputy catches his breath."
        print "He starts to say, 'Outlaws are coming into town! It's the 'Trio' gang!'"
        print "Just as he done talking the leader of the 'Trio' gang walks through the"
        print "front door, Bob grim is one mean looking outlaw and he has his eyes on you."
        print "Three things come to mind, 'draw', 'run', or 'challenge' bob to a dual."
        print "better decide fast his glare making you a little nervous..."
        print " "


        action = raw_input("> ")

        if action == "draw":
            print "That glare of Bobs got to you, drawing your pistol in your shakey hand,"
            print "you could not pull the trigger in time as Bob draws his pistol smoothly"
            print "and shoots you dead."
            print " "
            return 'death'

        elif action == "run":
            print "Bobs' glare has got your nerves shot, you decide to take the back exit as"
            print "you can, but Bob is no fool and he draws his pistol and shoots you in the"
            print "back until he runs out of bullets."
            print " "
            return 'death'

        elif action == "challenge":
            print "You muster up your courage and standing tall and proud. You issue your"
            print "challenge to Bob. Bob smirks at you and says 'Outside now'. You take one"
            print "more sip of your drink and head out the door for a show down."
            print " "
            return 'dual_part_1'

        else:
            print "Better make sense fast or your dead..."
            print "have your tried draw or run yet?"
            print "how about challenge?"
            print " "
            return 'bar'

class DualPart1(Scene):

    def enter(self):
    	print " "
        print "You make our way out to the center of town. You find Bob but he is not alone."
        print "He got his other outlaw buddies with him, on Bobs' left Joe with his beady "
        print "little eyes trained on you and on Bobs' right Phil with his crossed eyes"
        print "well looking likehe has make sure his nose is still there. They start to"
        print "draw their pistols, You are already sweating but you mangae to get your"
        print "mind running with options like:'draw' to shoot back, 'dive' left and"
        print "maybe take out beady eye Joe, or 'dodge' right and shoot crossed eyes"
        print "Phil right between the eyes."
        print " "

        action2 = raw_input("> ")

        if action2 == "draw":
            print "You draw your pistol smoothly and fire first, but it's tragic that your"
            print "shot failed to hit anyone before you can fire off another the 'Trio' unload"
            print "their bullets into you, only when the last shot is fired does your body"
            print "drop to the floor."
            print " "
            return 'death'

        elif action2 == "dive":
            print "You dive left, Bobs' shot misses you by mere inches, crossed eyes Phil"
            print "shots are totally off the mark, but beady eyed Joe held his shot till"
            print "your dive finished and shoots you right in the head, and then empty"
            print "the rest of his bullets into you."
            print " "
            return 'death'

        elif action2 == "dodge":
            print "You dodge right, Bobs' shots whiz right by your head, crossed eyes Phil is"
            print "shocked and his shots are way off mark, and beady eyed Joe only manages to"
            print "shoot your hat off your head, you draw your pistol and shoot crossed eyes"
            print "Phil right between the eyes. That's one down now two more to go..."
            print " "
            return 'dual_part_2'

        else:
            print "Better make sense fast or your dead..."
            print " "
            return 'dual_part_1'



class DualPart2(Scene):

	def enter(self):
		print " "
		print "With crossed eyes Phil dead, Bob is in shock that Phil is dead, and is not"
		print "paying attention to you but dead Phil, beady eyed Joe is reloading his gun"
		print "This is a chance to shoot 'Bob' dead and then take out 'Joe' or shoot 'Joe'"
		print "first as he is still reloading..."
		print " "

		action3 = raw_input("> ")

		if action3 == "Bob":
			print " "
			print "You figure why not take down the most toughest of the group and point"
			print "your pistol at Bob but before you can fire beady eyed Joe has reloaded"
			print "his gun and starts pumping bullets into you like no tomorrow. You drop"
			print "dead after the last shot."
			print " "
			return 'death'

		elif action3 == "Joe":
			print " "
			print "Well since Bob is not paying any mind to you, and beady eyed Joe is still"
			print "loading his gun, You take aim at beady eyed Joe. Beady eyed Joe in his"
			print "panic to load his gun faster fumbles his pistol and you shoot him dead."
			print "Bob realizing that Joe is dead too returns his attention back to you."
			print " "
			return 'dual_part_3'

		else:
			print "Better make sense fast or your dead..."
			print "Bob or Joe duh! pick one fast!"
			print " "
			return 'dual_part_2'


class DualPart3(Scene):

	def enter(self):
		print " "      
		print "Now it's just you and Bob, now the only problem is with all the shooting,"
		print "You dont know if you got any bullets left or if Bob has got bullets left."
		print "Do you take the chance and 'shoot' hoping to end it all now or 'reload'?"
		print "It all comes down to luck now..."
		print " "

		luck = "%s" % randint(1,2)

		action4 = raw_input("> ")

		if action4 == "shoot" and luck == "1":
			print "You go for it and point your pistol at Bob and pull the trigger!"
			print "Your pistol clicks, you try again and it clicks a few more times..."
			print "Bob starts to laugh and aims his pistol at you and pulls the triger."
			print "BANG! you drop dead."
			return 'death'

		elif action4 == "shoot" and luck == "2":
			print "You go for it and point your pistol at Bob and pull the trigger!"
			print "BANG! Bob looks dumbfounded with the new hole in his chest"
			print "Bob falls dead and you holster your pistol."
			return 'finished'

		elif action4 == "reload" and luck == "1":
			print "You reload your gun with grace and ease and aim your gun at Bob."
			print "BANG! Bob looks dumbfounded with the new hole in his chest"
			print "Bob falls dead and you holster your pistol."
			return 'finished'

		elif action4 == "shoot" and luck == "2":
			print "You start to reload your gun, in your haste you funble the bullets."
			print "Bob starts to laugh and aims his pistol at you and pulls the triger."
			print "BANG! you drop dead."
			return 'death'

		else:
			print "Better make sense fast or your dead..."
			return 'dual_part_3'

class Death(Scene):

    quips = [
        "You were out gunned, better luck next time.",
         "You're full of holes now.",
         "Here lies 'Sherif', got shot.",
         "Everybody is laughing at you now."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class Finished(Scene):

    def enter(self):
        print " "
        print "With all the outlaws dead, you decide to go celebrate with a drink at the bar."
        print "Everyone in town cheers your name and celebrates with you."
        return 'finished'