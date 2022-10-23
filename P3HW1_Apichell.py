

    # This program calculates grades and outputs the values as well as a letter value
    # 10/22/2022
    # CTI-110 P3HW1_Apichell
    # Colby Apichell
    # This program takes a number grade , determines average and displays letter grade for average.
    # 
    # All values outputs are formatted as a float with: variable_num = float(input('Enter Variable: '))
    #
    # 1.) Get the following variables, grades
    # 2.) Enter grades into a list
    # 3.) Determine lowest, highest , sum and average for grades
    # 4.) Determine letter grade for average
    # 5.) Output lowest, highest , sum and average for grades in a neat format
    # 6.) Output letter grade in a neat format
    # Formats for a two decimal float example:
    #                                         print({:0,.2f}'.format(your_variable_here))


# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6,]

#determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
sum_of_grades = sum(grades)
avg = (sum_of_grades / len(grades))

# determine letter grade for average
# Store letter grade as variable appropriately


if avg >= 90:
    final_grade = 'A'
if avg >= 80:
    final_grade = 'B'
else:
    final_grade = 'F'
    

#Output lowest, highest , sum and average for grades in a neat format
#Output letter grade in a neat format
    
print()
print('------------Results------------')
print('Lowest Grade:','    ',' {:0,.1f}'.format(low))
print('Highest Grade:','   ',' {:0,.1f}'.format(high))
print('Sum of Grades:','   ',' {:0,.1f}'.format(sum_of_grades))
print('Average:','         ',' {:0,.2f}'.format(avg))
print('---------------------------------------')
print('Your grade is:', final_grade)

# Add input to pause program at end until user presses key, allowing them to view grades in cmd prompt python until ready to close program.
input()




