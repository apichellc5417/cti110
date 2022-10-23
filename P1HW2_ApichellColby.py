    # This program calculates travel expenses
    # 9/19/2022
    # CTI-110 P1HW2 - Travel Expense
    # Colby Aoichell
    #
    # This program calculates travel expenses
    # First it asks for the following variables, Budget, Fuel cost, Lodging Cost, and food cost
    # Second, The food, fuel and lodging costs are added together under total expenses
    # Third, Total expenses are deducted from initial budget to give you remaining balance.
    # All inputas are printed along with calculated remaining balance information for the user.
    #
    #Math
    #
    #total_expenses = (gas_num + lodging_num + food_num)
    #remaining_balance = (budget_num - total_expenses)
    #

print('This program calculates and displays travel expenses.')
print()
budget_num = int(input('Enter Budget:'))
print()
travel_dest = input('Enter your travel destination:')
print()
gas_num = int(input('How much do you think you will spend on gas?'))
print()
lodging_num = int(input('Approximately how much will you need for accomodation/hotel?'))
print()
food_num = int(input('Last, how much do you need for food?'))

print('------------Travel Expenses------------')
print('Location:', travel_dest)
print('Initial Budget:', budget_num)
print()
print('Fuel:', gas_num)
print('Accomodation:', lodging_num)
print('Food:', food_num)
print()
total_expenses = (gas_num + lodging_num + food_num)
remaining_balance = (budget_num - total_expenses)
print('Remaining Balance:', remaining_balance)

