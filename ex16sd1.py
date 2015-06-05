from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Opening the file. Goodbye!"
target.truncate()

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "Now I'm going to write these to the file."

oneline = "%r \n %r \n %r \n" % (line1, line2, line3)

target.write(oneline)

print "And finally, we close it."
target.close()
