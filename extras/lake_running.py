import datetime
import time

LOOK_UP=1
ADD=2
CHANGE=3
DELETE=4
QUIT=5

MENU=[LOOK_UP,ADD,CHANGE,DELETE,QUIT]
def main():
    #CREATE AN EMPTY DICTIONARY
    lakes_and_times={}
    #initialize variabkle for choice
    choice=0
    #process the choice
    try:
        while choice != QUIT:
            choice=get_menu_choice()

            if choice==LOOK_UP:
                look(lakes_and_times)
            elif choice==ADD:
                add(lakes_and_times)
            elif choice==CHANGE:
                add_a_time(lakes_and_times)
            elif choice==DELETE:
                delete(lakes_and_times)
    except Exception as err:
        print(err)

def get_menu_choice():
    while True:
        try:
            choice =int(input('please select'))
        except ValueError:
            print('please make a valid selection')
            continue
        if choice not in range(1,5):
            print('PLEASE SELECT A VALID CHOICE')
            continue
        else:
            break
    return choice

def delete(lakes_and_times):
    lake=input('please enter the name of the lake you want to remove')
    if lake not in lakes_and_times.keys():
        print('this lake is not in our directory')
    else:
        lakes_and_times.pop(lake)
        print(f'the lake names {lake} has been removed')


def print_choice():
    print()
    print('Lake running')
    print('_________________')
    print('1 Look up a lake')
    print('2 Add a new lake')
    print('3 Add a time to an existing  lake ')
    print('4 Delete an lake')
    print('5 Quit the program')


def look(lakes_and_times):

    lake=input('please enter the name of the lake you are looking for')
    if lake not in lakes_and_times.keys():
        print('this lake is not in our directory')
    else:
        print(f'here are the times you entered  for lake {lake}')
        [print (i,sep=',')for i in lakes_and_times.get(lake)]
        print()

def  add(lake_and_times):
    lake=input(' please enter the name of the lake you wishh to add')
    if lake not in lake_and_times.keys():
        lake_and_times.put[lake]=[]
    else:
        print('lake already exists ')

def  add_a_time(lake_and_times):
    while True:
        try:
            lake=input('please enter the lake you would like to add a time')
        except KeyError:
            print('this lake is not in the list')
            continue
        else:
            break
    lake_and_times(lake).append(get_time(f'please enter the time for lake {lake}'))
    return lake_and_times


def get_time(prompt):
     while True:
         try:
             num=float(input(prompt))
         except ValueError:
             print('please enter  valid value')
             continue
         if num<0:
             print('must be greater thank 0')
             continue
         else:
             break
     return num