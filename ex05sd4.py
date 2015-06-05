print "This is a digit in the string using the d format -> %d " % 34
print

print "This is a string in the string using the s format -> %s " % "happy"
print

print "This is also a digit in the string using the i format -> %i " % 35
print

print "This is an octal value in the string using the o format "

print
print "So octal number outout of 9 (should be 11) -> %o " % 9

print
print "This is an obsolete type in the string using the u format -> %u " % 36
print "It does the same as the d and i format for digits."

print
print "for the lowercase hexadecial numbers we use the lowercase 'x' format"
print "The hexadecimal for 10 (should be 'a') %x " % 10

print
print "for the uppercase hexadecial numbers we use the uppercase 'X' format"
print "The hexadecimal for 10 (should be 'A') %X " % 10

print "for eponential floating point numbers we use the lowercase 'e' or uppercase 'E'"
print

print "for floating point decimals we can use the lowercase 'f' or uppercase 'F'"
print "so we can display decimal numbers like: %f and %F up to 6 decimal places" % (2.5, 5.1789321)
print

print "for more precise floating point numbers we have 'g' and 'G'"
print "it also limits to at least 5 places or less"
print " %g and %G" % (2.5, 5.1789321)
print

test = "6'2"
print "to display values as is we have the 'r' format, so it will have python display"
print "things in the raw format as it can be shown."
print "examples inclde numbers: %r, and stings: %r, and variables: %r." % (1234, 'happy', test)
print
