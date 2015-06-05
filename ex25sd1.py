print """the last few lines of the what you should see are:
ex25.print_first_and_last(sentence)
ex25.print_first_and_last_sorted(sentence)
"""

print
print """
The first one: 
ex25.print_first_and_last(sentence)

calls the function:
print_first_and_last(sentence)

a var is created equal to the function call of break_words 
with the 'sentence' input as an argument.

then the var is passed to the next function called:
print_first_word(words)

then passed to the next function called:
print_last_word(words)


The next function:
print_first_and_last_sorted(sentence)

This function starts the same but instead var equal to break_words()
it is equal to sort_sentence() which also calls break_words() 
equal to a var

then the var words is passed to the other function calls:
print_first_word(words)
print_last_word(words) 

and the function is then complete.
"""
