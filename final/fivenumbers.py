import re

def putInt(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Value must be a whole number")
            continue
        else:
            break
    return value

def get_num():
    nums=re.compile(r'/d,/d,/d,/d,/d')
    while False:

        getNums=input('please enter only 5 numbers 1-9 separated by commas like this "x,x,x,x,x')

        if getNums != nums:
            print('you must enter only 5 numbers 1-9 separated by commas like this "x,x,x,x,x')
            continue
        else:
            break
    return getNums.split(',')





def output(listofNums):
    print(listofNums)

if __name__ == '__main__':
    listofNums=get_num()
    output(listofNums)