print "Map of the game: "

print """

start() -> 1. "left"    -> bear_room()   
        -> 2. "right"   -> cthulhu_room()   
        -> 3. dead(why)
        
bear_room() -> 1. "take honey"                      -> dead(why)
            -> 2. "taunt bear" and not bear_moved   -> bear moves
            -> 3. "anything else typed"             -> "I got no idea what that means." -> bear_room()
            
bear_moved = true   -> 1. "taunt bear"  -> dead(why)
                    -> 2. "take honey"  -> dead(why)
                    -> 3. "open door"   -> gold_room()
                    -> 4. anything else -> "I got no idea what that means." -> bear_room()

gold_room() -> 1. amount entered < 50   -> "Nice, you're not greedy, you win!" -> exit(0)
            ->2. amount entered > 50    -> dead(why)

cthulhu_room()  -> 1. "flee"    -> start()
                -> 2. "head"    -> dead(why)
                -> 3. anything  -> cthulhu_room()
"""       
