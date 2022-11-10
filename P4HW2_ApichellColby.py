    # This program calculates MULTIPLE employee salaries and gives you a total block at the end for the sum of all overtime, hours worked, employees entered and other metrics.
    # 10/22/2022
    # CTI-110 P4HW2 - Employee salary
    # Colby Apichell
    # Create empty lists
    # Create a loop structure
    # Get/enter name of employee 
    # Get/enter number of hours employee worked
    # Get/enter employee pay rate
    # Determine if overtime is worked
    # Calculate overtime
    # If yes calculate amount owed due to overtime
    # Calculate amount employee should be paid for regular hours
    # Display gross pay
    # Display name, pay rate, number of hours worked, overtime hours, overtime pay , pay for regular hours and gross pay
    # Add all abovre values to our lists
    # Calculate the total of all values
    # Present values in the pertinent blocks below for user

# create some lists
employees_entered = 0
overtime_list = []
reg_hour_list = []
gross_pay_list = []

name = ''
# create our loops structure
name = str(input('Enter employee name or "None" to terminate: '))
while name != "None":
    is_overtime = False   
    hours_worked = float(input(f'How many hours did {name} work? :  '))
    pay_rate = float(input(f'What is {name} payrate?:  '))
    print
    reg_hour_pay = (hours_worked * pay_rate)

    if (hours_worked > 40.00):
        is_overtime = True
        hours_ov = (hours_worked - 40)

    else:
        is_overtime = is_overtime
        hours_ov = 0

    ### Calculate overtime

    if is_overtime:
        overtime_compensation_rate = (pay_rate * 1.5)
        total_ot_pay = (overtime_compensation_rate * hours_ov)
        
    else:
        total_ot_pay = 0
        reg_hour_pay = ((hours_worked - hours_ov) * pay_rate)  


    gross_pay = (reg_hour_pay + total_ot_pay)

    print()                                            
    print(f'Employee name: {name}')
    print()
    print('Hours Worked      Pay Rate     OverTime     OverTime Pay    RegHour Pay    Gross Pay')                                                                      
    print('----------------------------------------------------------------------------------')                                                                                                               
    print(f'{hours_worked:<18.1f}{pay_rate:<13.1f}{hours_ov:<13.1f}{total_ot_pay:<16.2f}${reg_hour_pay:<14.2f}${gross_pay:<10.2f}')
    print()
    name =str(input('Enter employee name or "None" to terminate: '))

    # Append or add all values to the lists so we can calculate them later

    employees_entered += 1
    overtime_list.append(total_ot_pay)
    reg_hour_list.append(reg_hour_pay)
    gross_pay_list.append(gross_pay)
    
    
# Math time
# Show the deets

    
   
print()
print(f'Total number of employees entered: {employees_entered}')
print(f'Total amount payed for overtime: {sum(overtime_list)}')
print(f'Total amount payed for regular hours: {sum(reg_hour_list)}')
print(f'Total amount paid in gross: {sum(gross_pay_list)}')
                                                            
