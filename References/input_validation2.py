""" This file is to play with some common input validation
strategies for numeric and string data"""

# Counting program with strategy to enforce
# positive whole numbers being entered...
# adapted from Dominic and improved by Mary
#with some more tweaking by DomiNic
print("Welcome to our counting program.")
print("It also adds up the digits that you count!")
startNum = input('Please enter a small number to start counting: ')
while startNum.isnumeric() is False or float(startNum) < 0:
    startNum = input('Please enter a positive whole number: ')
startNum = int(startNum)

stopNum = input('Now, enter a larger number to count up to: ')
while stopNum.isnumeric() is False or float(stopNum) < 0 or float(stopNum) <= startNum :
    stopNum = input(f'Enter a whole number greater than your start number {startNum}. ')
stopNum = int(stopNum)
# initialize totaling feature - adds up each digit counted
total = 0
for number in range(startNum, stopNum):
    print(number)
    total += number
print("The total of all the numbers you counted is: {:,d}.\n".format(total))


# This strategy enforces whole, positive #s are entered
# prevents empty entries too - adapted by Cecily & others
while True:
    nickles = input("How many nickles do you have? ")
    # Only allow positive integers
    if nickles.isnumeric() is False or float(nickles) < 0:
        print("Whole, positive numbers only please!")
        continue
    else:
        # Convert to int
        nickles = int(nickles)
        break
print(f'You have {nickles} nickles.')

# this strategy enforces a whole number - found by Nick, John M
# but it doesn't prevent negatives
while True:
    try:
        pennies = int(input('How many pennies do you have? '))
    except ValueError: # runs if type error occurs
        print('Please enter a whole number!\n')
        continue
    else:
        break
print(f'You have {pennies} pennies.\n')

# string validation - adapted from many students
color1 = input("Pick a primary color: red, yellow or blue: ")
color1 = color1.lower() # makes it case insensitive
while color1 not in ["red", "yellow", "blue"]: # uses a list data type
    color1 = input("Carefully enter one of these colors: red, yellow, blue: ")

if color1 == "red":
    color2 = input("Enter a second primary color: yellow or blue: ")
    color2 = color2.lower()
    while color2 not in ["yellow", "blue"]:
        color2 = input("Carefully enter one of these colors: yellow, blue: ")
elif color1 == "yellow":
    color2 = input("Enter a second primary color: red or blue: ")
    color2 = color2.lower()
    while color2 not in ["red", "blue"]:
        color2 = input("Carefully enter one of these colors: red, blue: ")
elif color1 == "blue":
    color2 = input("Enter a second primary color: red or yellow: ")
    color2 = color2.lower()
    while color2 not in ["red", "yellow"]:
        color2 = input("Carefully enter one of these colors: red, yellow: ")

print(f'You have chosen {color1} and {color2} as your two colors.')

'''Below are some functions we used over the summer '''

def inputPosInt(): # ensures "int-able" input over 0
    posInt = input('\tEnter a positive whole number: ')
    while posInt.isnumeric() is False or posInt == "0":
        posInt = input('\tPlease enter a whole number, greater than 0: ')
    posInt = int(posInt)
    return posInt


def inputPos0Float():  # ensures "floatable" input, 0 or greater
    pos0Float = input('\tEnter a decimal or whole number: ')
    while pos0Float == "" or pos0Float.isalpha() or float(
            pos0Float.isnumeric()) is False or float(pos0Float) < 0:
        pos0Float = input(
            '\tEnter only a decimal or whole number, 0 & up: ')
    pos0Float = float(pos0Float)
    return pos0Float

'''integer example cannot be broken '''
def get_pos_int(prompt):#using prompt in the function allows user to call "get" functions without defining see below
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if value < 0:
            print("Sorry, your response must not be negative.")
            continue
        else:
            break
    return value

if __name__ == '__main__':
    age=get_pos_int("please enter your age") #notice these functions need not be defined
    kids=get_pos_int("please enter how many kids")






''' another floatr example cannnot be broken!'''
def get_float(prompt):
    while True:
        try:
            flizzoat = float(input(prompt))
        except Exception as e:
            print(e)
            print("Must be a decimal number")
            continue
        if flizzoat<0:
            print('your float must be positive')
            continue
        else:
            break
    return flizzoat
if __name__ == '__main__':

  hourly_wage=get_float("please enter your hourly wage")

  print(f'you make ${hourly_wage:.2f} an hour')



