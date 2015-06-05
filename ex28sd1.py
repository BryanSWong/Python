print True and True       # true, got right
print False and True      # false, got right
print 1 == 1 and 2 == 1   # false, got right
print "test" == "test"    # true, got right
print 1 == 1 and 2 != 1   # true, got right
print True and 1 == 1     # true, got right
print False and 0 != 0    # true, got wrong its False so (False and False) = False
print True or 1 == 1      # true, got right
print "test" == "testing" # false, got right
print 1 != 0 and 2 == 1   # fasle, got right
print "test" != "testing" # true, got right
print "test" == 1         # false, got right
print not (True and False)    # true, got right
print not (1 == 1 and 0 != 1) # false, got right
print not (10 == 1 or 1000 == 1000)   # false, got right
print not (1 != 10 or 3 == 4) # false, got right
print not ("testing" == "testing" and "Zed" == "Cool Guy")   # true, got right
print 1 == 1 and (not ("testing" == 1 or 1 == 0))   # true, got right
print "chunky" == "bacon" and (not (3 == 4 or 3 == 3))    # false, got right
print 3 == 3 and (not ("testing" == "testing" or "Python" == "fun"))  # false, got right
