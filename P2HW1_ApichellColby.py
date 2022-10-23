    # This program calculates travel expenses
    # 10/06/2022
    # CTI-110 P2HW1 - Travel Expense
    # Colby Apichell
    # 
    # This program calculates travel expenses
    # All values are formatted as a float with: variable_num = float(input('Enter Variable: '))
    # 1.) Get the following variables, Budget, Fuel cost, Lodging Cost, and food cost
    # 2.) Add the food, fuel and lodging costs under total expenses
    # 3.) Subtract total expenses from initial budget to give you remaining balance.
    # 4.) All inputs are printed as so  with calculated remaining balance information for the user.
    #
    # Formats for dollar sign with a float example:
    #                                         print(${:0,.2f}'.format(budget_num))
    #
    #Math
    #
    #total_expenses = (gas_num + lodging_num + food_num)
    #remaining_balance = (budget_num - total_expenses)
    #

print('This program calculates and displays travel expenses.')
print()
budget_num = float(input('Enter Budget: '))
print()
travel_dest = input('Enter your travel destination: ')
print()
gas_num = float(input('How much do you think you will spend on gas? '))
print()
lodging_num = float(input('Approximately how much will you need for accomodation/hotel? '))
print()
food_num = float(input('Last, how much do you need for food? '))

print('------------Travel Expenses------------')
print('Location:','        ','',travel_dest)
print('Budget:','          ',' ${:0,.2f}'.format(budget_num))
print('Fuel:','            ',' ${:0,.2f}'.format(gas_num))
print('Accomodation:','    ',' ${:0,.2f}'.format(lodging_num))
print('Food:','            ',' ${:0,.2f}'.format(food_num))
print('---------------------------------------')
total_expenses = (gas_num + lodging_num + food_num)
remaining_balance = (budget_num - total_expenses)
print()
print('Remaining Balance:',' ${:0,.2f}'.format(remaining_balance))


