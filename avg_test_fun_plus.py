'''this program is average grade program modified using input validation library and numpy to show the power of the snake'''

import numpy as np
from library import inUtils as inu


def get_Input():
    return np.array([inu.putPosFloat(f'please enter test {i+1} ')for i in range(inu.posPutInt("how may test would you like to enter?"))])
def process_loop(students):
    for student in range (students):
        print (f'for student #{student+1}')
        nums = get_Input()
        print(f'for student #{student+1}')
        print_Output(nums)


def print_Output(nums):
    print(f" Total of  all {len(nums)} tests, is {np.sum(nums)} \n"
          f"The highest score is{np.max(nums)} \n"
          f"The lowest score is {np.min (nums)}\n"
          f"The average score was {np.mean(nums):.2f}\n"
          f"The total of the middle three scores is {np.sum(nums)-(np.min(nums)+np.max(nums))}")

if __name__ == '__main__':
    students=inu.posPutInt('How many students grades would you like to record')
    process_loop(students)



