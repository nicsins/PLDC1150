'''Author=_nic_
this program calculates perimeter
of a rectangle in sq inches
9/16/2018
this program tells them how to format'''

print("This program calculates the perimeter of a rectangle ")

#Gather user input and define variables
# (always do this before calculations)
unit=input('please select unit you are using to measure "cm,in ,ft ,m ,yds"?')
length=float(input("please enter the length of the rectangle "))
width=float(input("please enter the width of the rectangle in "))

#calculations !!(Always done after getting input and defining variables)

Perimeter=(length+width)*2

#display output (always the last thing!

print(f'The perimeter of the rectangle is {Perimeter:,.2f}  {unit}')
