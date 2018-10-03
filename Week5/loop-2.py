'''write a program that asks the user
for a small number then  a larger number
    author=__nic__
9/29/2018'''

#get user input and define variables with data validation

while True:
    try:
        small= int(input('please enter a small whole number'))
    except ValueError:
        print("Sorry, I need a whole number.")
        continue
    else:
        break
while True:
    try:
        big= int(input('please enter a larger whole number'))
    except ValueError:
        print("Sorry, I need a whole number .")
        continue
    if big<small:
        print("number must be larger than the first")
        continue
    else:
        break
# process loop

sum=0#initialize accumulator
for num in range(small,big +1):
    if num!=big:
        print(num,"+",end='')
    else:
        print(num,"=",end='')
    sum+=num
print(sum)