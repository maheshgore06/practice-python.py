name = str(input("Enter your name:"))
total_income = int(input("Enter your total income:"))
food_expence = int(input("Enter your food expence:"))
travel_expence = int(input("Enter your travel_expence:"))

Total_expence = food_expence + travel_expence
remaining_balance = total_income - Total_expence
print("Hello,",name,"!")
print("Your total income is:",total_income)
print("Your total expenses are:",Total_expence)
print("Your remaining balance is:",remaining_balance)