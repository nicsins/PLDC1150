'''author=_nic_
\one line and escape chars
09/16/2018'''
 #this is a one liner print statement
print('this is how we use escape charactors this is a tab\tthen you have a newline\n'
      'net you want single quotes\' then double quotes \" then tripple quotes  \'\'\' anothe new line \n'
      'then a backslash single \\   and a double backslash \\\\ i hope you get the point!')



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


''' math functions'''
import math

# round  up
print(round(6.66))
#square root
print(math.sqrt(3))
#i round to 3 places another way than format (this way rounds up)
print(round(6.6666667,3))

