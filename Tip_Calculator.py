print("Welcome to the tip calculator.")
tot_bill = float(input("What was the total bill? $"))
tip_per = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))
final_bill = tot_bill + (tot_bill * tip_per / 100)
bill_per_head = round(final_bill / num_people, 2)
print(f"Each person should pay: ${bill_per_head}")

