'''this program is average grade program modified using input validation library and numpy to show the power of the snake'''

import numpy as np
from library import inUtils as inu#input validation module


def get_Input():# this is only to gather input allows for varying length of tests
    return np.array([inu.putPosFloat(f'please enter test {i+1} ')for i in range(inu.posPutInt("how may test would you like to enter?"))])


def process_loop(students):#this essentially is the "main" but is trult the processing loop
    list_of_nums=[]
    for student in range (students):
        print (f'for student #{student+1}')
        nums = get_Input()
        print(f'for student #{student+1}')
        print_Output(nums)
        list_of_nums.append(nums)
    l_o_num=np.array(list_of_nums)#convert to numpy array
    #TODO make this section cleaner
    print_Output(l_o_num)


def print_Output(nums):#some of this function borrowed from a stack post
    print(f" Total of  all  tests, is {np.sum(nums)} \n"
          f"The highest score is {np.max(nums)} \n"
          f"The lowest score is {np.min (nums)}\n"
          f"The average score was {np.mean(nums):.2f}\n"
          f"The total of the other scores is {np.sum(nums)-(np.min(nums)+np.max(nums))}")


if __name__ == '__main__':
    students=inu.posPutInt('How many students grades would you like to record')
    process_loop(students)



