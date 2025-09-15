print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

total_tip=tip/100
total_tip_amount=bill* total_tip
total_bill=bill+total_tip_amount
total= total_bill/people
final_bill=round(total, 2)
print(f"each person should pay ${final_bill}")
