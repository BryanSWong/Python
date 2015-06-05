numbers = []

def test(top, step):
    i = 0
    while i < top:
        print "At the top i is %d" % i
        numbers.append(i)
    
        i = i + step
        print "Numbers are now: ", numbers
        print "At the bottom i is %d" % i


  
print "The numbers: "
test(9, 2)  
for num in numbers:
    print num
