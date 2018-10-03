def getInput():
    return [int(input(f'enter score for test # {i+1}'))for i in range( int (input('How many test scores would you like to enter')))]

def print_Output(nums):
    print('the values entered are ',end='')
    [print(i,' ',end='')for i in nums]
    print()
    print(f'The highesty score was  {max(nums)}')
    print(f'the lowest score was {min(nums)}')
    print(f'the average score is {sum(nums)/len(nums)}')
    print(f'the sum of all the scores is {sum(nums)}')
    print (f'the sum of scores minus highest and lowest is {sum(nums)-(max(nums)+min(nums))}')

if __name__ == '__main__':
    nums=getInput()
    print_Output(nums)