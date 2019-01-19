''' Mouhari Mouhamed  10-25-19 " ABC Company Widgets and Discounts
This program will determine how maany widges you purchase
and take the value to calculate a discount amount and give
custumer the discount price before ant taxes.'''

# Introduction to the customer

# list variables
discount = 0

def main():

    try: # exception handling
        numberOfwidgets= input1()
        discount=get_discount(numberOfwidgets)
        total, discounts, widgets = process(numberOfwidgets, discount)
        output(numberOfwidgets, discount, widgets, discounts, total)
    except Exception as e: # generic way to handle all exceptions
        print(e) # e is the variable name to call out that Exception

def input1():
    print("Welcome to ABC Widget!")

    while True:  # While loop to validate the user input
        try:
            numberOfwidgets = int(input("How many widgets do you want to buy? "))
        except ValueError:
            print("Value must be a valid number")
            continue  # if there is an error the loop will continue
        if numberOfwidgets < 0:
            print("ERROR: response must be greater than 0")
            continue
        else:
            break # if condition is met the loop breaks
    return numberOfwidgets

def get_discount(numberOfwidgets):
    discount=0
    if numberOfwidgets >= 100:
        discount = 40
    elif numberOfwidgets > 50:
        discount = 30
    elif numberOfwidgets > 20:
        discount = 20
    elif numberOfwidgets > 10:
        discount = 10
    elif numberOfwidgets >= 0:
        discount = 0


    return  discount # return value


# proccesing the data
def process(numberOfwidgets, discount):
    widgets = 99 * numberOfwidgets
    discounts = (discount / 100) * widgets
    total = widgets - discounts
    return total, discounts, widgets



# displaying there total and output
def output(numberOfwidgets,discount,widgets,discounts,total):
    print(f"You are buying {numberOfwidgets} widgets, earning a {discount:.1f}% discount.")
    print(f"Retail price @ $99 ea:  ${widgets:>9,.2f}")
    print(f"Amount you saved today: ${discounts:>9,.2f}")
    print(f"Discount price b4 tax:  ${total:>9,.2f}")

main() # call main to start the program
