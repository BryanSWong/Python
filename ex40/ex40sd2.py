class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
test = "It might seem crazy what I'm about to say", "Sunshine she's here, you can take a break", "I'm a hot air balloon that could go to space", "With the air, like I don't care baby by the way"

test2 = "I had a dream so big and loud", "I jumped so high I touched the clouds", "I stretched my hands out to the sky", "We danced with monsters through the night"


test3 = "Happy birthday to you", "I don't want to get sued", "So I'll stop right there"

test4 = "They rally around tha family", "With pockets full of shells"

 
happy_bday = Song(test3)
                   
bulls_on_parade = Song(test4)


happy = Song(test)
              
best_day_of_my_life = Song(test2)



happy_bday.sing_me_a_song()
print
bulls_on_parade.sing_me_a_song()
print
happy.sing_me_a_song()
print
best_day_of_my_life.sing_me_a_song()
print
