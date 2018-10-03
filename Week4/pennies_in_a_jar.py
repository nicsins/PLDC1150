'''author=_nic_
program that asks the user to enter
 a number of pennies in a jar
 9/18/2018'''

#get user input

amount=input('Please enter how many pennies are in your jar')
while amount == '' or amount.isalpha() or float(amount.isnumeric()) == False or float(
        amount) < 0 :
    print('must be a number and greater than 0 ')
    amount=input('Please enter how many pennies are in your jar')
amount=int(amount)

#conditional logic to give output
if amount>100:
    print('You have more than a dollar')
elif amount<100:
    print('You have less than a dollar')
else:
    print("You have exactly a Dollar")