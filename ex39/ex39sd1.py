# create a mapping of state to abbreviation
states = {
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'Wisconsin': 'WI'
}

# create a basic set of states and some cities in them
cities = {
    'WI': 'Madison',
    'WA': 'Olympia',
    'VI': 'Richmond'
}

# add some more cities
cities['UT'] = 'Salt Lake City'
cities['VT'] = 'Montpelier'

# print out some cities
print '-' * 10
print "UT State has: ", cities['UT']
print "VT State has: ", cities['VT']

# print some states
print '-' * 10
print "Wisconsin's abbreviation is: ", states['Wisconsin']
print "Washington's abbreviation is: ", states['Washington']

# do it by using the state then cities dict
print '-' * 10
print "Wisconsin has: ", cities[states['Wisconsin']]
print "Washington has: ", cities[states['Washington']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)
    
# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)
    
# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])
    

print '-' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Tennessee')

if not state:
    print "Sorry, no Tennessee."
    
# get a city with a default value
city = cities.get('TN', 'Does Not Exist')
print "The city for the State 'TN' is: %s" % city
