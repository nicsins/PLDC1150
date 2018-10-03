'''avg grade'''
grades=[int(input(f'Enter test score {i+1}')) for i in range (int(input(('How many test scores would you like to enter' ))))]
print(f'The average of {len(grades)} scores is {sum(grades)/len(grades):.2f}')
[print(i,' ',end='')for i in grades]
print()

'''wage calc'''
ot=1.5
othours=0
wage=float(input('how much per hour'))
hours=int(input('how many hours'))
if(hours>40):
    othours=hours-40
    reghours=40
else:
    reghours=hours
gross=(reghours*wage)+(othours*(wage*ot))
print(f"your gross pay is ${gross:.2f}")

'''bus practice'''
reg_ride=7
rush_ride=12
reg_rate=1.75
rush_rate=3

total_reg=reg_ride*reg_rate
total_rush=rush_ride*rush_rate
total_fare=rush_ride+reg_ride
print("Bus Fare Program")
print('{:.<15}{:<15}{:<15}{:<15}'.format('Type Ride','Cost Rides','# Rides','Total cost'))
print('_'*60)
print('{:.<15}${:.<14.2f}{:.<15}${:.<14.2f}'.format('Reg  Ride',reg_ride,reg_ride,total_reg))
print('{:.<15}${:.<14.2f}{:.<15}${:.<14.2f}'.format('Rush Ride',rush_rate,rush_ride,total_rush))
print('The total Cost  for all rides is $',format(total_fare,'.2f'))

print(len("\t"))

print(f'the total fare is ${total_Fare:.2f} ')