perfect_numbers = []
for x in range(1,10000):
	S = 0
	for y in range(1,x-1):
		if x % y == 0:
			S = S + y
	if S == x:
		perfect_numbers.append(x) 	
l = len(perfect_numbers)
for x in range(l):
	print(perfect_numbers[x])
