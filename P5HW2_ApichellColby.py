    # This program uses a menu to generate a math quiz.
    # 11/29/2022
    # CTI-110 P5HW2 - Math Quiz
    # Colby Apichell
    #




import random
import time

def rand_num():
    num1 = random.randint(0,100)
    num2 = random.randint(0,100)
    return num1, num2


def adding_rand_num(num1, num2):
    print(f'   {num1}')
    print(f' + {num2}')
    answer_key = num1 + num2
    user_answer = -99
    guesses = 0

    while user_answer != answer_key:
        user_answer = int(input('Type Your answer:'))
        if user_answer > answer_key:
            print('Too high, try again!')
            guesses += 1
            
            
        elif user_answer < answer_key:
            print('Too low, try again!')
            guesses += 1
            
        else:
            guesses += 1
            print('Congratulations!!!! your answer is correct..')
            print(f'Number of guesses: {guesses}')
            menu()
            
            
            
            
        

def sub_rand_num(num1, num2):
    print(f'   {num1}')
    print(f' - {num2}')
    answer_key = num1 - num2
    user_answer = -99
    guesses = 0

    while user_answer != answer_key:
        user_answer = int(input('Type Your answer:'))
        if user_answer > answer_key:
            print('Too high, try again!')
            guesses += 1
            
            
        elif user_answer < answer_key:
            print('Too low, try again!')
            guesses += 1
            
        else:
            guesses += 1
            print('Congratulations!!!! your answer is correct..')
            print(f'Number of guesses: {guesses}')
            menu()
    








def menu():
    print()
    print('MAIN MENU')
    print('--------------------')
    print('1. Adding Random Numbers')
    print('2. Subtracting Random Numbers' )
    print('3. Exit')

    option = int(input('Please choose one of the menu options: '))
    num1, num2 = rand_num()
    if option == 1:
        adding_rand_num(num1, num2)
    elif option == 2:
        sub_rand_num(num1, num2)
    elif option == 3:
        print('Thank you for playing...')
        print('Bye!!')
        time.sleep(2)
        quit()
    else:
        print('Enter a valid option!')
        menu()
    
     
menu()

    
