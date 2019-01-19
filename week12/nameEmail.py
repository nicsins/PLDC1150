def main():
    try:
        display_choice()
        display_Menu()
    except Exception as err:
        print(err)

def display_choice():
    print('make a choice')
    print('type 1 for add')
    print('type 2 for view')
    print('type 0 for quit')

def display_Menu():
    commands=[0,1,2]
    cmd=''
    while True or cmd not in [0,1,2]:
        cmd=input('please enter a selection')
        if cmd=="1":
            contacts = get_Contacts()
            writeToFile(contacts)
        elif cmd=="2":
            readFile()
            readLines()
        elif cmd=="0":
            print('thank you for playing please come again')
            break
        else:
            print('make a valid selection')

def get_Contacts():
    return[ name for name in input('please enter name(s) and email(s) dividing each set by a coma').split(',')]


def writeToFile(contacts):
    myFile = open('contacts.txt', 'a')
    [myFile.write(name+'\n') for name in contacts]
    myFile.close()
    return myFile


def readFile():
    myFile = open('contacts.txt','r')  # r for read mode
    myData = myFile.readline() # read one line at a time
    while myData != "":
        print(myData.rstrip("\n"))  # delete newline character
        myData = myFile.readline() # read one line at a time
    myFile.close()  # close the file
    print()   # blank line

def readLines():
   # myFile = open('contacts.txt', 'r')  # r for read mode
    [print(lines.rstrip())for lines in open('contacts.txt', 'r') .readlines()]
   # [print(lines.rstrip())for lines in myFile.readlines()]
    #myFile.close()






if __name__ == '__main__':
    main()


