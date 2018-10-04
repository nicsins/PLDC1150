""" this program breaks up perimeter program into functions"""

def main(): #recursive funtion that calls the order of the defined functions in the program below
    try:
        length=get_length()
        width=get_width()
        perimeter=calculate_perimeter(length,width)
        display_output(perimeter)
        not_again()
    except Exception as e:#handles all errors not caught in defining the variables
        print(e)
#askes user for valid positive number for length
def get_length():
    while True:#data validation loop
        try:
            length = float(input('Please enter the length of your quadralateral'))
        except ValueError as e: #this gives user a message of improper value entered
            print(e)
            print("Must be a valid number")
            continue
        if length<0: # checks number is greater than 0
            print('your length must be positive')
            continue
        else:
            break
    return length
#askes user for valid positive number for width
def get_width():
    while True:#data validation loop
        try:
            width = float(input('Please enter the width of your quadralateral'))
        except ValueError as e:
            print(e)
            print("Must be a valid number")
            continue
        if width<0 : # checks number is greater than 0
            print('your width must be positive')
            continue
        else:
            break
    return width

def calculate_perimeter(length,width):
    perimeter=2*(length+width)
    return perimeter
   # return 2*(length+width) this is will also work

def display_output(perimeter):
    print(f'The perimeter of the quadrilateral is {perimeter:,.2f} undefined units')

def not_again():
    again = input('press y to continue an other key to quit')
    while again == 'y':
        main()

if __name__ == '__main__':
    main()