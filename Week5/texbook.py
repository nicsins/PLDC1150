''' texbook program
author =__DomiNic__
this is an example program of ways to
use data validation for integers and floats
along with presenting a solid example of nested loops
**improved from lab notes***'''

print('Welcome to the book shop')
#start with getting user input and defining variables
head="*"*40#simple decoration
print(head)

while True:
    #ask number of books as a string
    items =input('How many books is the customer buying? ')

    if not items.isnumeric():# isnumeric evaluates strings not int or float
        print("number must be a whole number greater than 0")
        continue
    elif int(items)<1:# cast as int to check if greater than zero only after the numeric condition is met
        print('must be greater than zero')
        continue
    else:#cast as integer and break the validation loop
        items=int(items)
        total = 0.0#initialize accumulator
        for item in range(items):#initialize for loop
            while True:#data validation for a float
                try:#exception handling checks for value error first
                    price = float(input(f'Enter price of item #{item + 1}: '))#user input displays iteration
                except ValueError:
                    print('enter a proper price in numbers ')
                    continue# if there is an error loop continues
                if price<0:#conditional loop checks for number less than 0
                    print('muust be greater than 0')
                    continue
                else: #all conditions met loop is broke
                    break
            total = total + price # after data is validated accumulation occurs
            if item!=(items-1): # conditional loop to ensure logical output
                print(f'{"Running subtotal":.<30}${total :<8.2f}')
            else:
                break
        #final informitive output displayed
        print(f'{"Grand total":.<30}${total :<8.2f}')#double quotes must be used for any strings withing {} formatting
        #caculations in formating allowed when value is not repeated
        print(f'{"Average price per book":.<30}${total/items :<6.2f}')
        print(head)
    #ask user to quit
    close = input('Time to close? Enter y to quit any other key to continue:').lower()#turns to lowercase in case y is Y
    if close == 'y':
        break
print(head)
print('Thanks for using the program')
