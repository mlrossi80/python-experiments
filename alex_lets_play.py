first = "Hello, "
second = "what is your name?"

original = raw_input(first + second)

while True:
	if original.isalpha():
	    name = original
	    next_step = raw_input("Hello, " + name + ". Would you like to play a game?") 
	    print next_step
	else:
	    print "Come again?"
	    original = raw_input(second)
	    
	# if len(next_step) > 0 and next_step == "y" or "Yes":
	#     print "Very good! Let's play!"
	# else:
	# 	print "Get out, then!"