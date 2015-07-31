directions = ["north", "south", "east", "west", "down", "up", "left", "right", "back"]
verbs = ["go", "stop", "kill", "eat", "beat", "punch", "run"]
stopWords = ["the", "in", "of", "from", "at", "it"]
nouns = ["door", "bear", "princess", "cabinet", "pot", "honey", "gold"]

def covert_numbers(s):
	try:
		return int(s)
	except ValueError:
		return None

def scan(string):
	case = string.lower()
	test = case.split(" ")
	hold = []
	for word in test:
		if word in directions:
			direct = ('direction', word)
			hold.append(direct)
		elif word in verbs:
			verb = ('verb', word)
			hold.append(verb)
		elif word in stopWords:
			stop = ('stop', word)
			hold.append(stop)
		elif word in nouns:
			noun = ('noun', word)
			hold.append(noun)

		elif word.isdigit():
			number = ('number', covert_numbers(word))
			hold.append(number)
		else:
			wrong = ('error', word)
			hold.append(wrong)	
	return hold