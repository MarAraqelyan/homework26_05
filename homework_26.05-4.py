year = int(input("Enter a year:"))
year_count=0
for x in range(1600,year):
    if x % 4==0 or (x % 100==0 and x%400==0):
        year_count = year_count + 1
print(year_count)
