# define the function cheese_and_crackers and give it variables and code to do 
# something
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blancket.\n"
    
    
# This part of the code shows you can give it normal hard coded values
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

#This part of the code shows you can use variables for arguments in your funciton
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# this part of the code shows you can use math equations as arguments for your 
# functions
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


# this part of the code shows you can use a combination of math equations and 
# variables for arguments in your functions

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) 
