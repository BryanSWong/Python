numbers = []

def test(max):
    i = 0
    while i < max:
        print "At the top i is %d" % i
        numbers.append(i)
    
        i = i + 1
        print "Numbers are now: ", numbers
        print "At the bottom i is %d" % i


  
print "The numbers: "
test(9)  
for num in numbers:
    print num
