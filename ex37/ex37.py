print """ 

flow charts are normal use with boxes with actions 
in them and arrows that point to other actions, or 
even problems in them with arrows to solutions.

and example flow chart would be a map of my game 
from chapter 36 homework.

from the top down:

                              start()
           /            /               \               \           \ 
    north_room()   south_room()    east_room()      west_room()    death
        |         /  |  \           /   \               |
      death  death death death  death  new_room()     death
                                      /   |    \
                                 death  death  fill bowl
                                                 |
                                             pull rope
                                                |
                                            open door
                                               |
                                           last_room()
                                           /       \
                                        death      Win game
"""
