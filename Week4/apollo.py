''' author=-nic_
asks user what year we landed on the moon and
tells you if you got it right
09/18/2018'''

#get user input establish var
right_year=1969
year = input('What year did Apollo 11 land on the moon? ')
while year== '' or year.isalpha():
    year = input('What year did Apollo 11 land on the moon? ')

year=int(year)

if year == right_year:
    print(f'Correct! {year} is right!')
elif abs(year-1969)<=10:
    print(f'you are within {abs(year-1969)} years')
else :
    print(f'Sorry, {year} is the wrong answer.')

