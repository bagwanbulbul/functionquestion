def say_hello_language(name, language):
	if language == "hindi":
		print "namste", name
		print "Aap kaise ho?"
	elif language == "punjabi":
		print "sat sri akaal",name
		print "thuada ki hal hai?"
	else:
		print "hello", name
		print "how are you?"
say_hello_language("rishab", "punjabi")
say_hello_language("arman", "english")
say_hello_language("abhishek", "french")
say_hello_language("kavay", "hindi")