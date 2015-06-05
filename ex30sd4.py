people = 30
cars = 40
trucks = 15

# if cars is greater the people print statement.
if cars > people:
    print "We should take the cars."
# else if cars less then people print statement.
elif cars < people:
    print "We should not take the cars."
# otherwise print this statement if cars not greater then or less then people.
else:
    print "We can't decide."

# if trucks greater then cars print statement.  
if trucks > cars:
    print "That's too many trucks."
# if trucks less then cars then print this statement.
elif trucks < cars:
    print "Maybe we could take the trucks."
# otherwise print this statement if trucks not greater then or less then cars
else:
    print "We still can't decide."

# if people is greater then trucks print this statement    
if people > trucks:
    print "Alright, let's just take the trucks."
# otherwise print this statement.
else:
    print "Fine, let's stay home then."
