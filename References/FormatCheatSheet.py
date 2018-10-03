# formatting samples
#Use the format() function to round decimals:
print(format(12345.6789, '.1f'))
print(format(12345.6789, '.2f'))
#Add comma separators:
print(format(12345.6789, ',.2f'))
#Specify the minimum column width:
print(format(12345.6789, '12.2f'))
#line up numbers on the decimal place
num1 = 123.456
num2 = 1.2345
num3 = 123456.56789
print('Number 1', format(num1, '12.2f'))
print('Number 2', format(num2, '12.2f'))
print('Number 3', format(num3, '12.2f'))

#use format to generate a % format
print(format(0.5, '%'))
print(format(0.5, '.0%'))

#Use the format() function to format an integer:
print (format(123456, '10,d'))
#'0,d' easy integer with , separator
#'d' for integer! Who knew?

#dollar signs
grossPay = 843.7
print("Gross Pay = $" + str(format(grossPay,'.2f')))

'''Here is some practice with the new era formatting.
Suppose this code is part of a retail cash system.
Provides line item cost and reward info
Look at the pretty print out when you run it.'''
itemPrice = 12.99  #price of an item
itemQuantity = 5  #number of items purchased

itemSubtotal = itemQuantity * itemPrice #receipt line item subtotal
discount = .05 #loyalty program discount rate

cashBack = itemSubtotal * discount #cash back to members
itemDue = itemSubtotal - cashBack #how much they owe

print("{:<13}$ {:>7.2f}".format("Item total:", itemSubtotal))
print("{:<13}$ {:>7.2f}".format("Cash back:", cashBack))
print("{:<13}$ {:>7.2f}".format("Amount Due:", itemDue))


city = "Minneapolis"
temp = 67
chanceRain = 40
gasPrice = 2.50
guests = 1000
print("Welcome! Around the {} Hilton we have…".format(city))
print("{0:<14}{1:^14}{2:^14}{3:^14}".format("Temperature", "Chance Rain", "Gas Price", "Guests"))
print("{0:>5d}f \t\t{1:>9d}% \t\t\t${2:<9.2f}{3:^14,d}".format(temp, chanceRain, gasPrice, guests))

city = "Minneapolis"
temp = 67
chanceRain = 40
gasPrice = 2.50
guests = 1000
print("Welcome! Around the {} Hilton we have…".format(city))
print("{0:<14}{1:^14}{2:^14}{3:^14}".format("Temperature", "Chance Rain", "Gas Price", "Guests"))
print("{0:>5d}f \t\t{1:>9d}% \t\t\t${2:<9.2f}{3:^14,d}".format(temp, chanceRain, gasPrice, guests))
# dollar formatting
coffee_cost=100.00
print(f"A coffee costs {f'${coffee_cost:.2f }':<20} ")
print("A coffee costs {0:<20}".format("${0:.2f }".format(coffee_cost)))  # non-shorthand

print("A coffee costs {0:20}".format(f'${coffee_cost:.2f }'))


#time and date input

import time,datetime

t= time.ctime()
f = datetime.datetime.strptime(t, '%a %b %d %H:%M:%S %Y')
print (f)
from datetime import datetime
d = datetime.now()
d.strftime('%m/%d/%Y %H:%M:%S')

d = datetime.strptime(time.ctime(),"%a %b %d %H:%M:%S %Y")

d.strftime('%m/%d/%Y %H:%M:%S')

#table formt with f string

'''Author = _name_
proigram calculates gross sales in a coffeee shop'''
#get user input
cupsCoffee=int(input('How many cups coffee'))
cupsTea=int(input('How many cups tea'))
cupsCap=int(input('How many cups cappuccino'))
costCoffee=float(input("how much per cup of Coffee"))
costTea=float(input("how much per cup of Tea"))
costCap=float(input("how much per cup of cappuccino"))

coffee_sales=cupsCoffee*costCoffee
tea_sales=cupsTea*costTea
cap_sales=cupsCap*costCap
total_sales=coffee_sales+tea_sales+cap_sales
print(f'the gross total sales  was ${total_sales:.2f}')
print('{:<20}{:<11}{:<6} {:<10}'.format("Drink Type","Cost","#drink","Tot/Drink"))
print("-"*50)
print(f'{"Coffee":.<20}${costCoffee:<10.2f}{cupsCoffee:<6}${coffee_sales:<10.2f}')
print(f'{"Tea":.<20}${costTea:<10.2f}{cupsTea:<6}${tea_sales:<10.2f}')
print(f'{"Cappuccino":.<20}${costCap:<10.2f}{cupsCap:<6}${cap_sales:<10.2f}')
print(f'the gross total sales  was ${total_sales:.2f}')




#more formatting with good commenting


'''double discount program this adds two discounts together
 you buy something at a store and you get the daily discount 
plus good customer discount output is new price formatted in table form'''

#define variables gather input

daily_discount=.10
customer_discount=.05
price=float(input("please enter the cost of your items before the discount"))
#calculations
new_price=price*(1-(daily_discount+customer_discount))#if it was tax you would add to the 1
#display output
print(f'{"Original price":<20}${price:.>9.2f}')
print(f'{"Customer discount":<20}{customer_discount:.>10.0%}')
print(f'{"Daily  discount":<20}{daily_discount:.>10.0%}')
print(f'{"Discounted price":<20}${new_price:.>9.2f}')

