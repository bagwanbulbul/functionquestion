def calculator(n, n1, opreation):
	if opreation == "add":
		number1 = n+n1
		add_result = number1
		print "add opreation = ",number1
		return number1
	elif opreation == "subtract":
		number2 = n-n1
		add_subtract = number2
		print "subtract opreation = ",number2
		return number2
	elif opreation == "multiply":
		number3 = n * n1
		add_multiply = number3
		print "multiply opreation = ",number3
		return number3
	elif opreation == "divide":
		number4 = n/n1
		add_divide = number4
		print "divide opreation = ",number4
		return number4
n = int(raw_input("enter the number"))
n1 = int(raw_input("enterr the second number"))
calculator(n,n1, "add")
calculator(n, n1, "multiply")
calculator(n, n1, "divide")
calculator(n, n1, "subtract")
