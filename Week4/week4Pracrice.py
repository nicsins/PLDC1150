''' author=_name_
program determines grade by inputting a score
9/18/2018'''

#gather user input
score = input('Enter quiz score: ')
# validation block
while score == '' or score.isalpha() or float(score.isnumeric()) == False or float(
        score) < 0 or float(score)>100:
    print('Try the program again, and enter\n'
          ' positive numbers only between 1 and 100')
    score = input('Enter quiz score: ')
score=int(score)

#conditional loop to determine grade
if score >= 90:
    print('Grade: A')
elif score >= 80:
    print('Grade: B')
elif score >= 70:
    print('Grade: C')
elif score >= 60:
    print('Grade: D')
else:
    print('You did nopt pass please try again.')


''' college program'''


college = input('Please enter your college: ')

if college == 'Minneapolis College':
    print('Good choice!')
else :
    print('You should go to Minneapolis College!')