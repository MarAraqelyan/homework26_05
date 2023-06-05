while True:
	print("Enter two numbers")
	x=float(input("x="))
	y=float(input("y="))
	if not x + y == 0:
		break
print(abs(x-y)/(x+y))
