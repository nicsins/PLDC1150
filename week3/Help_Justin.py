#Justin Peterson 9/14/2018
#This program will ask the user for the length of a rectangle, ask for width,
#and will calculate the area and display in a sentence.


#square_feet = length_feet * width_feet
#square_centimeters = length_centimeters * width_centimeters

# square_inches = length_inches * width_inches
# #TODO Move the calculations to after the gathering of input
# print('Welcome to the Rectangle Area Calculator!')
# inches = str(input('What is your measurement unit (in., ft., cm. etc.? '))
# #TODO remove unneeded input statements
# length_inches = float(input('What is the length of the rectangle in inches? '))
# width_inches = float(input('What is the width of the rectangle in inches? '))
#
#
# print('Your rectangle is' + str(format(square_inches, '.2f')), 'square inches.')
print('Welcome to the Rectangle Area Calculator!')
units = input('What is your measurement unit (in., ft., cm. etc.? ')
length = float(input('What is the length of the rectangle in inches? '))
width = float(input('What is the width of the rectangle in inches? '))
AREA = length * width
print('Your rectangle is ' + str(format(AREA, '.2f')), 'square inches.')

