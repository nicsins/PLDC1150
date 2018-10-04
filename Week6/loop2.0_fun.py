""" this is a program that asks for two numbers then adds up all the numbers between and including those numbers. there is data validation included as well and the program is divided into functions"""


#this is a recursive function that defines the main function which then calls all the other functions
def main():
    try:#this try and except will handle any possible errors not caught already
        small = get_small()
        big = get_big(small)
        print_numbers( small,big)
        not_again()
    except Exception as e:# this part is a generic variable "e" that will tell the print fuction to print a nice message to the user why there is an error
        print(e)



#this functions asks the user for the first number and checks if it is a whole number above zero
def get_small():
    while True:# this loop will not stop until the condition is satisfied
        try:#using try /except/if /else to validate data
            small = int(input('Please enter a small greater than 0'))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if small < 0:
            print("Sorry, your response must not be negative.")
            continue
        else:
            break
    return small#returns value to be used anywhere else needed
#this function ask and checks for a valdi whole number greater than the first number
def get_big(small):
    while True:
        try:   #using try /except/if /else to validate data
            big = int(input('Please enter a big greater than 0'))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if big< small:
            print("sorry number must be lkarger than the first number")
            continue
        else:
            break
    return big

# this function loops and adds up all the numbers between small and big printing out the output during the loop
def print_numbers(small,big):
    sum=0
    for num in range(small, big + 1):
        if num != big:
            print(num, "+ ", end='')
        else:
            print(num, "= ", end='')
        sum += num
    print(sum)

def not_again():
    again=input('press y to continue an other key to quit')
    while again =='y':
        main()





if __name__ == '__main__':
   main()#calls main function


