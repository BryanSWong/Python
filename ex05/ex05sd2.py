name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # pounds
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
kilos = weight * .453592
centimeters = height * 2.54

print "Let's talk about %r." % name
print "He's %r inches tall, or %d centimeters tall." % (height, centimeters)
print "He's %r pounds heavy, or %d kilos heavy." % (weight, kilos)
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %r, %r, and %r I get %r." % (age, height, weight, age + height + weight)