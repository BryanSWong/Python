from sys import argv

script, input_file = argv

# define first function which reads your txt file given.
def print_all(f):
    print f.read()
    
# define second function
def rewind(f):
    f.seek(0)
    
# define third function
def print_a_line(line_count, f):
    print line_count, f.readline()
    
# create the var current_file that opens your input_file arg(should be a text 
# file)    
current_file = open(input_file)


print "First let's print the whole file:\n"

# calls your first function
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# calls your second function
rewind(current_file)

print "Lets print three lines:"

# create a counter var called current line.
current_line = 1

# calls the third function and used the values from vars as arguments
print_a_line(current_line, current_file)

# update the counter to the next number or state. calls third function again
current_line = current_line + 1
print_a_line(current_line, current_file)

# updates one last time and calls the function for the last time. 
current_line = current_line + 1
print_a_line(current_line, current_file)
