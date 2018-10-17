''' how to import a local module '''
from library import inUtils as inu
import re
def get_Input(): #formal way to define a function
    return inu.putPosFloat('enter a positive valid (floating point)')
if __name__ == '__main__':
   # email=inu.isEmail('enter a valid email')

    ip=inu.isIp('enter your ip address')

    validNum=inu.phone('enter a valid phone number')

    pozFliz=get_Input() #call function in main

    pozint=inu.posPutInt('Enter a positive whole number') #return variable without defining function

    NEint=inu.putInt('Enter any whole number')

    NEflot=inu.putFloat('Enter any valid number(floating point)')



