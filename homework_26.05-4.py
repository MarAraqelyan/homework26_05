while True:
	year = int(input("Enter a year:"))
	if not year // 1600 == 1:
 		break
year_count=0
if year // 1600 > 0:
	for x in range(1600,year):
		if x % 4 == 0:
			if x % 100 == 0:
				if x % 400 == 0:
					year_count += 1
			else:
				year_count += 1
if year // 1600 == 0:
	for x in range(year,1600):
		if x % 4 == 0:
			if x % 100 == 0:
				if x % 400 == 0:
					year_count += 1

			else:
				year_count += 1

print(year_count)
