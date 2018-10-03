'''game that selects a secret number between 1 - 20 ,if they dont get it right  the proigram gives a hint whether odd or even on the 2nd wrong they oofffer higher and lower'''
import random
def get_number():
    return random.randint(1,20)
def get_Input():
    num=input('guess a number between 1 and 20')
    while num.isnumeric() is False or int(num)<0:
        num = input('guess a number must be  between 1 and 20')
    return  int(num)
def process_loop(num,answer):

    if(num!=answer and num %2==0):
        print("wrong guess number is even")
        get_Input()
        process_loop2(num,answer)
    elif (num!=answer and num%2!=0):
        print('number is odd ')
        get_Input()
        process_loop2(num,answer)
    else:
        print('Correct')
def process_loop2(num,answer):

    if(num!=answer and num>answer):
        print('your guess is less than the secret number')
        get_Input()
        process_loop2(num,answer)
    elif(num!=answer and num<answer):
        print('Your guess is greater than the secret number')
        get_Input()
        process_loop2(num,answer)
    else:
        print('Correct')






if __name__ == '__main__':

    answer=get_number()
    print(answer)
    num=get_Input()
    process_loop(num,answer)