"""Author = __name__
This program calculates gas
 """

# define variables
#TODO what are my variables ask user for miles driven,number of gallons and price of gas
#TODO miles=int(input('How many miles driven?'))
#TODO gallons_used=int(input('hoe many gallons used?'))
#TODO price_per_gallon=float(input('what is the cost per gallon?'))
miles=int(input('How many miles driven?'))
gallons_used=int(input('hoe many gallons used?'))
price_per_gallon=float(input('what is the cost per gallon?'))

#do calculations
#TODO do my calculaions fuel cost and miles /gal
#TODO MPG=miles/gallons_used
#TODO total_cost=price_per_gallon*gallons_used

#do my calculaions fuel cost and miles /gal
MPG=miles/gallons_used
total_cost=price_per_gallon*gallons_used


#display output
#TODO print(f'total miles driven {miles:5,d}')
#TODO print(f'total gallons used{gallons_used:5,d}')
#TODO print(f'total miles /gallon {MPG:5,.2f}')
#TODO print(f'total cost of trip ${total_cost:10,.2f}')
print(f'total miles driven {miles:5,d}')
print(f'total gallons used{gallons_used:5,d}')
print(f'total miles /gallon {MPG:5,.2f}')
print(f'total cost of trip ${total_cost:10,.2f}')