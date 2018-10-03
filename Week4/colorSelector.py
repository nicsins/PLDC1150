

'''color selector modified from Mary and my work'''

#define colors

color_1=''
color_2=''
newColor=''

# string validation - adapted from many students
color1 = input("Pick a primary color: red, yellow or blue: ")
color1 = color1.lower() # makes it case insensitive
while color1 not in ["red", "yellow", "blue"]: # uses a list data type
    color1 = input("Carefully enter one of these colors: red, yellow, blue: ")

if color1 == "red":

    color2 = input("Enter a second primary color: yellow or blue: ")
    color2 = color2.lower()
    while color2 not in ["yellow", "blue"]:
        color2 = input("Carefully enter one of these colors: yellow, blue: ")
elif color1 == "yellow":
    color2 = input("Enter a second primary color: red or blue: ")
    color2 = color2.lower()
    while color2 not in ["red", "blue"]:
        color2 = input("Carefully enter one of these colors: red, blue: ")
elif color1 == "blue":
    color2 = input("Enter a second primary color: red or yellow: ")
    color2 = color2.lower()
    while color2 not in ["red", "yellow"]:
        color2 = input("Carefully enter one of these colors: red, yellow: ")
red=print("\033[31m Red")
blue=print("\033[34mBlue")
yellow=print("\033[93m Yellow")
orange=print("\033[33m orange")
purple=print("\033[35m purple")
green=print("\033[32m  green")


if (color1=="red" and color2=='yellow') or (color2=='red' and color1=='Yellow'):
    color_1=red
    color2=yellow
    newColor=orange
elif (color1=="red" and color2=='blue') or (color2=='red' and color1=='blue'):
    color2=blue
    color_1=red
    newColor=purple
else:
    color_1=blue
    color2=yellow
    newColor=green

print(f'You have chosen {color1} and {color2} as your two colors.')
print(f'these two colors make {newColor}')
