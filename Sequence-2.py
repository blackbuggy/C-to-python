# WAP to read the number of days from user and conver it into years, months and remaining days.


x = int(input("Enter number of days: "))


years = x // 365


months = (x - years *365) // 30


days = (x - years * 365 - months*30)


print("Years = ", years)
print("Months = ", months)
print("Days = ", days)
