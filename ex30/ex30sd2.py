people = 20
cars = 25
trucks = 30

# this statement will not be printed
if cars > people:
    print "We should take the cars."
# this statement will be printed
elif cars < people:
    print "We should not take the cars."
# this statement will not be printed
else:
    print "We can't decide."

# this statement will be printed   
if trucks > cars:
    print "That's too many trucks."
# this statement will not be printed
elif trucks < cars:
    print "Maybe we could take the trucks."
# this statement will not be printed
else:
    print "We still can't decide."
    
if people > trucks:
    print "Alright, let's just take the trucks."
# this statement will be printed
else:
    print "Fine, let's stay home then."
