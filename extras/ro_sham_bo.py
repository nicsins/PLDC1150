'''ro sham bo no function'''
import time
import random
print('Lets play rock paper scissors!')
time.sleep(1)
again='y'
choices=['rock','scissors','paper']
while again=='y':

    choice=random.choice(choices)
    while True:
        your_choice=input("choose 'rock','scissors','paper'")
        if your_choice not in choices:
            print("you must choose 'rock','scissors','paper'")
            continue
        else:
            break
    print(f'computer choses {choice}')
    time.sleep(1)
    if (choice=='rock'and your_choice=='paper')or (choice=='scissors'and your_choice=='rock')or (choice=='paper'and your_choice=='scissors'):
        print(f'{your_choice} beats {choice} ')
        time.sleep(.5)
        print('you win!;)')
    elif choice==your_choice:
        time.sleep(.5)
        print('players tie!')
    else:
        time.sleep(1)
        print(f'{choice} beats {your_choice} you lose :(')
    again=input('press y to play again any other key to quit').lower()