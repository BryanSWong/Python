# states the number of cars
cars = 100
# states the space avalable in cars
space_in_a_car = 4.0
# states the total number of drivers
drivers = 30
# states the number of passegers
passengers = 90
# states number of cars not used
cars_not_driven = cars - drivers
# states how many cars are in use
cars_driven = drivers
# states the amount of people that can fit into the carpool
carpool_capacity = cars_driven * space_in_a_car
# states the average number of passengers need per car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars avaliable."
print "There are only", drivers, "drivers avaliable."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
