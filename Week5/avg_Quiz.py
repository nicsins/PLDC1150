""" avg grade"""

while True:
    try :
        students=int(input("enter number of student"))
    except ValueError:
        print('must be a valid number')
        continue
    if students<0:
        print('must be greater than 0')
        continue
    else:
        break
while True:
    try:
        Tests= int(input("enter number of tests"))
    except ValueError:
        print('must be a valid number')
        continue
    if students < 0:
        print('must be greater than 0')
        continue
    else:
        break
for student in students:
    for test in Tests:
        print(f'for student{student+1} enter quiz # {test+1}')


