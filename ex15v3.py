# calls a module called argument variable argv
from sys import argv

# give the argv some arguments to work with
script, filename = argv

# sets variable txt to open the inputed filename argument
txt = open(filename)

# display a line about what your filename argument was
print "Here's your file %r:" % filename
# displays the command of reading what was in your filename given
print txt.read()
print txt.close()

# display text asking for the name of your filename again
print "Type the filename again:"
# a prompt that sets a variable to equal the input from user in this case filename
file_again = raw_input("> ")

# set a variable to open the previious input from user
txt_again = open(file_again)

# displays the var with the read of the filename inputed
print txt_again.read()
print txt_again.close()
