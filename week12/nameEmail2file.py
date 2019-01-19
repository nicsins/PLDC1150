def main():
    display()
    runProgram()



def decor(func):
    def wrap(*args):
        print('*'*40)
        func()
        print('*'*40)


def display():
    print('COMMAND MENU')
    print('1-Add number file')
    print('2- View number file')
    print('0-Exit program')

def runProgram():

    file=open('finalContacts.txt','w')

    while True:
        cmd=input('Enter a command')
        if cmd=='1':
            line = add()
            writeToFile(line)
        elif cmd=='2':
            view()
        elif cmd=='0':
            print('Thanks for playing')
            file.close()
            break
        else:
            display()
            cmd=input('Enter a command')
def add():
    numb=input('please enter 5 numbers divided by coma ","! ').rstrip(',')
    total=0
    total=sum(list(map(int,numb.split(','))))
    line=(numb,',',str(total))
    return line

def writeToFile(line):
    myFile = open('finalContacts.txt','a')
    myFile.write(line+'\n' )
    myFile.close()
    return myFile

@decor
def view():
    header = '1st,2nd,3rd,4th,5th,sum'.split(',')
    [print(f'{i:5}',end='')for i in header]
    print()
    fileRead=open('finalContacts.txt','r')
    reader=fileRead.read().split('/n')
    for lines in reader:
        [print(f'{i:<5}',end='')for i in lines.split(',')]
        print()
if __name__ == '__main__':
    main()