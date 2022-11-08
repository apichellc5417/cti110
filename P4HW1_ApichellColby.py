#### FINISHED ####


# CTI-110
# P4HW1 - Score List
# Colby Apichell 
# 11/08/2022
#
# This program allows the user to enter multiple scores and then drops the lowest score.
# The program then averages the scores and outputs rlevant data in the box below.


# create a blank list

# ask for number of scores

# input scores

# is score valid?

# do some math, dropping lowest score and averaging

# show grade and relevant data


scores = []

entries = 1


num_scores = int(input('How many scores would you like to enter? '))

while entries <= num_scores:
    print(f'Enter score #{entries}: ', end = ' ')
    new_score = int(input())
    if new_score < 0 or new_score > 100 :
        print('INVALID score entered!!!!')
        print('Score shoud be between 0 and 100')
        print(f'Enter score {entries} again: ')
        print()
              
    else:
        scores.append(new_score)
        entries += 1

low = min(scores)
high = max(scores)

scores.remove(low)

sum_of_grades = sum(scores)
avg = (sum_of_grades / len(scores))


if avg >= 90:
    final_grade = 'A'
elif avg >= 80:
    final_grade = 'B'
elif avg >= 70:
    final_grade = 'C'
elif avg >= 60:
    final_grade = 'D'
else:
    final_grade = 'F'



print()
print('------------Results------------')
print(f'Lowest score   : {low:.1f}')
print('Modified List  :', scores)
print('Scores Average : {:0,.2f}'.format(avg))
print('Grade          :',final_grade)                      
print('---------------------------------------')
