"""
Program: adventure.py
Author:  Sullayman Samai

Purpose: Adventure Game
"""

name = input('What is your name? ')

top_option = input(f'Hi {name}! What game you want to play [Football, Basketball, Tennis]: ')

if top_option.lower() == 'football':

    option1_sub_option = input('Are you good in playing football [Yes, No]: ')

    if option1_sub_option.lower() == 'yes':

        print('Okay that\'s good!')
        inner_option = input('Can we play now [Yes, No]: ')

        if inner_option.lower() == 'yes':
            print('Let\'s enjoy playing Football!')

        elif inner_option.lower() == 'no':
            print('Let\'s play another time. Thank you.')

    elif option1_sub_option.lower() == 'no':

        print('That\'s okay, I will teach you.')
        option1_inner_option = input('Are you willing to learn [Yes, No]: ')
            
        if option1_inner_option.lower() == 'yes':
            print('Let\'s enjoy learning Football!')
        elif option1_sub_option.lower() == 'no':
            print('Let\'s play another game. Thank you.')

elif top_option.lower() == 'basketball':
    print('Okay. That\'s good. Let\'s play Basketball.')

elif top_option.lower() == 'tennis':
    print('Okay. That\'s good. Let\'s play Tennis.')

else:
    print(f'Okay. That\'s good. Let\'s play {top_option}')