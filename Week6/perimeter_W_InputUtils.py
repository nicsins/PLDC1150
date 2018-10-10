from library import inUtils as inu

def main():
    try:
        length=inu.putPosFloat('Please enter the length of your quadralateral')
        width=inu.putPosFloat('Please enter the width of your quadralateral')
        perimeter=calculate_perimeter(length,width)
        display_output(perimeter)
        not_again()
    except Exception as e:
        print(e)

def calculate_perimeter(length,width):
    return 2*(length+width)

def display_output(perimeter):
    print(f'The perimeter of the quadrilateral is {perimeter:,.2f} undefined units')

def not_again():
    again = input('press y to continue an other key to quit')
    while again == 'y':
        main()
if __name__ == '__main__':
    main()