def add_numbers(num1, num2):
    print "This is the first number: %d" % num1
    print "This is the Second number: %d" % num2
    print "this is the numbers added together: %r" % (num1 + num2)
     
print "The first way"
print add_numbers(1, 2)
print 

print "The second way"
value1 = 1
value2 = 2
print add_numbers(value1, value2)
print

print "The third way"
print add_numbers(1 + 2, 3 + 4)
print

print "The fourth way"
print add_numbers(value1 + 2, value2 + 3)
print

print "The fifth way"
print "Enter the first value: ",
first = int(raw_input())
print "Enter the second value: ",
second = int(raw_input())
print add_numbers(first, second)
print
