''' this program asks user for the price of the meal
and the % tip  the user intends to give
the tax rate at7.5% the output should be a nicely formatted receipt   '''
#print intro
print('Welcome to Bobs Diner')
#define variable get user input
tax=.075
price=float (input('please enter the price of the meal'))
tip=float(input('Please enter the % tip you would like to leave'))*.01
#Do calculationsd

tip_amt=price*tip
tax_amt=price*tax
total=price+tip_amt+tax_amt

#print Output
print(f'{"Meal Price":<15}${price:<6.2f}')
print(f'{"Tip Amount:":<15}${tip_amt:<6.2f}')
print(f'{"Tax Amount:":<15}${tax_amt:<.2f}')
print(f'{"Total Due:":<15}${total:<.2f}')

print('\nThanks for dining @ Bobs!')
