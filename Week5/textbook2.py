'''textbook buying program while loop validation' some exception handling '''

#get user input how many books

books=input('How many books will you be buying?')#must ask for user input as a string in order to validate with next line

while books.isnumeric() is False or int(books)<0:#checking input withg isnumeric() function (boolean works on strings only this will also check against wild card chars) int(books) is used to cast string as integer so that you can check against an integer

    books=input('Please enter a positive whole number ')#when the input comes back as not valid you ask again

books=int(books)#cast user input into an integer

sum=0 # initial  ize the accumulator so that you can total all the books
for book in range(books):# initialize the for loop using the singular book as the counter for "books"

    while True:#initialize while True for data validation of a float
        try:# now using exception hanfling to check for a value as a way to validate
            cost=float(input(f'how much for book {book+1}'))#in this instance you can ask for a float
            #( book+1 )because the counter starts at 0
        except ValueError:# this will catch an improper value

            print("must be a proper value")
            continue# this will keep the loop going

        if cost <0:# using a conditional loop to ensure the value is greater than zero
            print('your float must be positive')
            continue
        else:
            break   #finallt=y when all conditions are met the "While "loop is broken and the other "For" loop continues

    sum=sum+cost # this will add up each iteration of cost to become the sum
#loop is completed and the output is displayed
print(f'The total amount of all the books you bought is ${sum:.2f}\n'
      f'the average cost  per book is ${sum/books:.2f}') #when  a variable isnt needed more than once it can be expressed as a calculation