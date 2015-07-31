True and True       # true, got right
False and True      # false, got right
1 == 1 and 2 == 1   # false, got right
"test" == "test"    # true, got right
1 == 1 and 2 != 1   # true, got right
True and 1 == 1     # true, got right
False and 0 != 0    # true, got wrong its False so (False and False) = False
True or 1 == 1      # true, got right
"test" == "testing" # false, got right
1 != 0 and 2 == 1   # fasle, got right
"test" != "testing" # true, got right
"test" == 1         # false, got right
not (True and False)    # true, got right
not (1 == 1 and 0 != 1) # false, got right
not (10 == 1 or 1000 == 1000)   # false, got right
not (1 != 10 or 3 == 4) # false, got right
not ("testing" == "testing" and "Zed" == "Cool Guy")   # true, got right
1 == 1 and (not ("testing" == 1 or 1 == 0))   # true, got right
"chunky" == "bacon" and (not (3 == 4 or 3 == 3))    # false, got right
3 == 3 and (not ("testing" == "testing" or "Python" == "fun"))  # false, got right
