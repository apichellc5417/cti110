    # This program calculates salary
    # 10/22/2022
    # CTI-110 P2HW1 - Travel Expense
    # Colby Apichell
    #
    # Get/enter name of employee 
    # Get/enter number of hours employee worked
    # Get/enter employee pay rate
    # Determine if overtime is worked
    # Calculate overtime
    # If yes calculate amount owed due to overtime
    # Calculate amount employee should be paid for regular hours
    # display gross pay
    # display name, pay rate, number of hours worked, overtime hours, overtime pay , pay for regular hours and gross pay
    #


is_overtime = False   
name = str(input('Enter you name here: '))
hours_worked = float(input('Enter your hours in this format 00.00, IE 24.00 hours:  '))
pay_rate = float(input('Enter your payrate in this format 00.00, IE $15.00 per hour:  '))
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


print('-------------------------------------                                                                                                                                                                                                   ')                                              
print(f'  Employee name: {name}                                                                                                                                                                                                                ')
print('                                                                                                                                                                                                                                        ')
print(' Hours Worked      Pay Rate     OverTime     OverTime Pay    RegHour Pay    Gross Pay                                                                                                                                                   ')                                                                      
print('----------------------------------------------------------------------------------                                                                                                                                                      ')                                                                                                               
print(f'{hours_worked:<19.1f}{pay_rate:<13.1f}{hours_ov:<13.1f}{total_ot_pay:<16.2f}${reg_hour_pay:<14.2f}${gross_pay:<10.2f}')
                                                        

