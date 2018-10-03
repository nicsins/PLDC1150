score = input('Enter quiz score: ')
# validation block
if score == '' or score.isalpha() or float(score.isnumeric()) == False or float(score) < 0:
    print('Try the program again, and enter positive numbers only')
else:
    score = float(score)
    if score >= 90:
        print('Grade: A')
    elif score >= 80:
        print('Grade: B')
    elif score >= 70:
        print('Grade: C')
    else:
        print('Your grade is undefined.')
