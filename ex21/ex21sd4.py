# for study drill part four make a simple formula and use the functions to make it.
def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b
    
def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b
    
def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b
    
def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

added = add(5, 5)
subtracted = subtract(10, 5)
multiplied = multiply( 5, 5)
divided = divide(120, 2)

# The formula is divide the adding of mutiplication of a subtraction
# divie(divided, add(added, multiply(multiplied, subtract(subtracted, 3))))

simple = divide(divided, add(added, multiply(multiplied, subtract(subtracted, 3))))

print "The formula result is equal to: ", simple
print
