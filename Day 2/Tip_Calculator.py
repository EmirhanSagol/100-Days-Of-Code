print("Welcone to the tip calculator")
bill = float(input("What was the total bill?"))
percantage = float(input("What pertentage tip would you like to give? 10, 12 or 15?"))
split = int(input("How many people to split the bill?"))
pay = (bill / split) * (percantage + 100) / 100
rounded_pay = "{:.2f}".format(pay)
print(round(pay, 2))
