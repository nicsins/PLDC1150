
def getInput():
    print('how many numbers',end='')
    items=inputPosInt()
    list=[]
    for num in range(items):
        print('enter number',end='')
        number=inputPosInt()
        list.append(number)
    return list
def displayOutput(list):
    [print(num, ' ', end='', ) for num in list]
    print(f'the total of numbers entered is {sum(list)}')



def inputPosInt(prompt): # ensures "int-able" input over 0
    posInt = input(prompt)
    while posInt.isnumeric() is False or posInt == "0":
        posInt = input('\tPlease enter a whole number, greater than 0: ')
    posInt = int(posInt)
    return posInt

if __name__ == '__main__':
    list=getInput()
    displayOutput(list)
