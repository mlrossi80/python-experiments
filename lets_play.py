first = "Hello, "
second = "what is your name?"

original = raw_input(first + second)
if len(original) > 0 and original.isalpha():
    next_step = raw_input("Hello, " +   original + ". Would you like to play a game?") 
    print next_step
else:
    print "Come again?"
if len(next_step) > 0 and next_step == "y" or "Yes":
    print "Very good! Let's play!"
else:
	print "Get out, then!"