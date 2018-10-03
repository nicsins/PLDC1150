'''week 5 examples'''
# answer = input('When did Apollo 11 land on the moon? ')
# while answer != '1969':		# if this is True, go into the loop
#     print('Wrong, try again')
#     answer = input('Enter the year when Apollo 11 landed on the moon: ')
# print('You are correct!')


""" while with validation """
while True:
    try:
        answer=int(input("When did Appollo 11 land on the moon?"))
    except ValueError:
        print("please enter valid input")
        continue
    if  answer <0:
        print("must be a valid year")
        continue
    elif answer!=1969 and abs(answer-1969)<10:
        print('getting close please try again')
        continue
    elif answer != 1969:
        print('wrong answer please try again')
        continue
    else:
        print("correct")
        break



""" another while loop"""
books_needed = int(input('How many textbooks do you have to buy? '))
book_counter = 1
total_cost = 0.0
while book_counter <= books_needed:    # test the condition
   price = float(input(f'Enter price of book #{book_counter}: '))
   total_cost = total_cost + price
   book_counter = book_counter + 1 # add 1 to the counter, each time thru the loop
print(f'All the books cost ${total_cost :<.2f}.')


''''nested loops'''
while True:
    print('Welcome to the book shop.')
    total = 0.0
    items = int(input('How many books is the customer buying? '))

    for item in range(items):
        price = float(input(f'Enter price of item #{item + 1}: '))
        total = total + price
        print(f'Running subtotal = ${total :<.2f}')
    print(f'Grand total = ${total :<.2f}')
    print(f' The average cost of your textbooks was ${sum/items:.2f} per book ')
    close = input('Time to close? Enter y or n:')
    if close == 'y':
        break
print('Thanks for using the program')



