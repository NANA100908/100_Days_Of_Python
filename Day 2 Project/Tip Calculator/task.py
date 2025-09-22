print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What Percentage tip would you like to give? 10 12 15"))
people = int(input("How many people to split the bill?"))
bill_with_pert = bill + (bill* (tip/100))
final_amt = bill_with_pert/people
print(f"Each Person should pay ${final_amt}.")