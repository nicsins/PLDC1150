import numpy as np
from library import inUtils as inu

def get_Input():
    return np.array([inu.putPosFloat(f'please enter test {i+1} ')for i in range(inu.posPutInt("how may test would you like to enter?"))])


def print_Output(nums):
    print(f" Total of  all test is {len(nums)} is {np.sum(nums)} \n"
          f"The highest score is{np.max(nums)} \n"
          f"The lowest score is {np.min (nums)}\n"
          f"The average score was {np.mean(nums)}\n"
          f"The total of the middle three scores is {np.sum(nums)-(np.min(nums)+np.max(nums))}")

    if __name__ == '__main__':
        nums = get_Input()
        print_Output(nums)

