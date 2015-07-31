# create a var with the r formatter 4 times
formatter = "%r %r %r %r"

# prints the formatter with the following inputs it will print them no matter
# what they are.
print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
# this formatter will use the original var a the inputs
print formatter % (formatter, formatter, formatter, formatter)
print formatter % ( "I had this thing", "that you could type up right",
                    "But it didn't sing", "So I said goodnight.")
