"""  Author=__Nic__
this is a detailed description of a program  that calculates the average grade of students"""


#define main
def main():
    try:#exception handling
        print_intro()
        students=get_Students()#call  input functions
        quizzes=get_Quizzes()
        get_student_avg(students, quizzes) # call processing loop
    except Exception as e: # this exception is generic way ton handle all exceptions
        print(e) # e is a variable used to signify exception
def print_intro():
    print('This program is used to calculate the average \n'
          'score of quiz scores entered from each student')
# asks user how many students
def get_Students():
    while True:# loop to make sure you get a positive whole number
        try:
            students = int(input("how many students"))
        except ValueError:
            print("Value must be a whole number")
            continue # if there is an error (input of wrong data type)the loop will continue

        if students < 0:
            print("Sorry, your response must not be negative.")
            continue
        else:
            break # if the condition is met the loop breaks
    return students# returns value
# asks user for number of quizzes checks for valid data
def get_Quizzes():
    while True:
        try:
            quizzes = int(input("How many quizzes per student"))
        except ValueError:
            print("Value must be a whole number")
            continue

        if quizzes < 0:
            print("Sorry, your response must not be negative.")
            continue
        else:
            break

    return quizzes
# this function asks user to enter scores for each student and then calculates and displays the average quiz score for that student
def get_scores(quizzes,student):
    total=0
    for quiz in range (quizzes):
        while True:# data validation using exception handling and if/else loop to ensure aonly a valid number is entered
            try:
                score = float(input(f'please enter the score for quiz# {quiz+1}'))
            except ValueError:
                print("Value must be a valid  number")
                continue

            if score < 0:
                print("Sorry, your response must not be negative.")
                continue
            else:
                break
        total+=score #total=total+score
    average=total/quizzes
    #call output function
    print_output(student, average)


def print_output(student,average):
    #prints the average score of each student
    print(f'the average quiz score for student# {student+1} is {average:.2f}')

#this funtion uses loop to get  the avreage score for every student using the "get_Scores" function"
def get_student_avg(students,quizzes):
    for student in range(students):
        print(f'for student # {student+1}')
        get_scores(quizzes, student) #recursive function

def not_again():
    while True:
        again=input("enter y and enter to run program again,\n"
                    " press any other key(s) and enter to quit").lower()
        if again=="y":
            main()
        else:
            print('Thanks for using ths program')
            exit()
if __name__ == '__main__':

    main() #call  the main function