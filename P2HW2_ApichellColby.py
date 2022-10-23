# CTI-110
# P2HW2 - List
# Colby Apichell
# 10/12/2022
#
# A calculator that calaculates grade averages
# Get inputs for modules as floats
# Store inputs in a list
# Print the, Lowest, highest, sum, and average grades below from said list
# math funtions used are basic list functions,  min(some_list), max(), sum(),
# avg is sum() / len()

 
module1_grade = float(input('Enter grade for Module 1: '))
module2_grade = float(input('Enter grade for Module 2: '))
module3_grade = float(input('Enter grade for Module 3: '))
module4_grade = float(input('Enter grade for Module 4: '))
module5_grade = float(input('Enter grade for Module 5: '))
module6_grade = float(input('Enter grade for Module 6: '))

grades_list = [module1_grade, module2_grade, module3_grade, module4_grade, module5_grade, module6_grade,]

print()
print('------------Results------------')
print('Lowest Grade:','    ',' {:0,.1f}'.format(min(grades_list)))
print('Highest Grade:','   ',' {:0,.1f}'.format(max(grades_list)))
print('Sum of Grades:','   ',' {:0,.1f}'.format(sum(grades_list)))
print('Average:','         ',' {:0,.2f}'.format(sum(grades_list) / len(grades_list)))
print('---------------------------------------')
