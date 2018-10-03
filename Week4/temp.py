''' author=_Nic_
program tells you if its cold
9/18/2018'''

#get user input

temp=input("Please enter the Temperature")
#validation loop for temp
while temp == '' or temp.isalpha():
    print("please enter a number")
    temp = input("Please enter the Temperature")




temp=float(temp)

if temp>0:
    print(f'The temperature {temp}  is greater than 0 degrees– thankfully!')
elif temp <0:
    print(f'The temperature {temp}  is less than 0 degrees - brrr!')

else:
    print(f'The temperature is exactly zero degrees- it figures')

print('That\'s all folks!')
