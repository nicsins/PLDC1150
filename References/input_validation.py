""" This file is to play with some common input validation
strategies for numeric and string data"""

# number validation - whole number - adapted from Nick, John M & ?
while True:
    try:
        pennies = int(input('How many pennies do you have? '))
    except ValueError: # runs if type error occurs
        print('Please enter a whole number!\n')
        continue
    else:
        break
print(f'You have {pennies} pennies.\n')

# number validation - whole number and positive
while True:
    nickles = input("How many nickles do you have? ")
    # Only allow positive integers
    if not nickles.isnumeric() or float(nickles) < 0:
        print("Whole, positive numbers only please!")
        continue
    else:
        # Convert to int
        nickles = int(nickles)
        break
print(f'You have {nickles} nickles.')
'''string validation - adapted from many students '''

color1 = input("Pick a primary color: red, yellow or blue: ").lower() # makes it case insensitive
while color1 not in ["red", "yellow", "blue"]:           # uses a list data type
    color1 = input("Carefully enter one of these colors: red, yellow, blue: ").lower()

if color1 == "red":
    color2 = input("Enter a second primary color: yellow or blue: ").lower()

    while color2 not in ["yellow", "blue"]:
        color2 = input("Carefully enter one of these colors: yellow, blue: ").lower()
elif color1 == "yellow":
    color2 = input("Enter a second primary color: red or blue: ").lower()

    while color2 not in ["red", "blue"]:
        color2 = input("Carefully enter one of these colors: red, blue: ").lower()
elif color1 == "blue":
    color2 = input("Enter a second primary color: red or yellow: ").lower()

    while color2 not in ["red", "yellow"]:
        color2 = input("Carefully enter one of these colors: red, yellow: ").lower()

if color1=="red "and color2=="yellow" or color1=="yellow"and color2=="red ":
    new_color="orange"
elif color1=="red "and color2=="blue" or color1=="blue"and color2=="red ":
    new_color='purple'
else:
    new_color="green"
print(f'You have chosen {color1} and {color2} and these colors mixed make {new_color}.')



