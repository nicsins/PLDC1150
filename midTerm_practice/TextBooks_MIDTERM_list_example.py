''' __author__=__DomiNic__
this program asks user for the cost of each textbook they purchased for the semester then displays the information in a nice table format
any attempt at using this program in your exam without demonstration of your working knowledge of these concepts will result in a disaster for you
with that i hope this is helpful'''



BOOKS=['Data-Com','SQL Server','ITEC Skills','Intro to Python ']#this is a globaL variable can be used in all functions without calling the function

def main():# this is where the programmer tells the computer the order of  the functions

    try:
        costs=get_costs()
        display_output(costs)
    except Exception as e:
        print(e)

def get_costs():#remember that 'BOOKS' is a GLOBAL VARIABLE(look this up if you do not know what it is and that the only reason it does not need to be called.
    costs=[]
    for item in BOOKS:
        price=pos_float(f'Enter cost for {item}')
        costs.append(price)
    return costs



def display_output(costs):
    print("Here's your overall budget:")
    print('{:<20}{:<20}{:<20}{:<20}'.format(*BOOKS))#using the *List format allows programer to save a couple lines of code and it looks alot cooler doesnt it?
    print('${:<19,.2f}${:<19,.2f}${:<19,.2f}${:<19,.2f}'.format(*costs))
    print(f'\nYour total monthly budget is ${sum(costs):,.2f}')

def pos_float(prompt):  # input validation using exception handling and conditional loop
    #using (prompt) allows the user to type whatever they want in the paren() like this
    # price=pos_float(f'please enter the price for {item}') this can be used with int all you have to do is change 'float' to 'int'
    while True:
        try:
            num = float(input(prompt))
        except ValueError:# if an improper value is entered then you will be asked the question again using this mix of while true and exception handling
            print(' Must be a valid whole number')
            continue
        if num < 0:
            print('number must be greater than zero')
            continue
        else:
            break
    return num


main()