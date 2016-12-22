first = "Hello, "
second = "what is your name?"

original = raw_input(first + second)
name = original
next_step = raw_input("Hello, " +   name + ". Would you like to play a game?") 

if original.isalpha() and len(original) > 0:

    print next_step
else:
    print "Come again?"

if  next_step == "y" or "Yes":
    print "Very good! Let's play!"
else:
	print "Get out, then!"