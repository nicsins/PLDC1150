def main():
    try:
        num_students, num_quizzes = get_input()
        list_of_list = processing(num_students, num_quizzes)
        display(list_of_list)
        restart = input('\nDo you want to restart? y or n')
        if restart == 'y':
            main()
    except Exception as err:
        print(err)

def get_input():
    num_students = pos_int_input('How many students are in the group?') # call to int validation function
    num_quizzes = pos_int_input('How many quizzes do they take?')  # call to int validation function
    return num_students, num_quizzes

def pos_int_input(prompt):  # called in both inputs and processing functions

    while True:
        try:
            pos_int = int(input(prompt))
        except ValueError:
            print('must be a whole number')
            continue
        if pos_int<0:
            print('Must be greater than 0')
            continue
        else:
            break

    return pos_int

def processing(num_students, num_quizzes):

    list_of_list=[]
    for student in range(num_students):
        list_of_scores=get_avg(student,num_quizzes)
        list_of_list.append(list_of_scores)


    return list_of_list


def get_avg(student,num_quizzes):
    list_of_scores=[]
    print(f'\nQuiz info for student #{student + 1}: ')
    for quiz in range(num_quizzes):
        quiz_score = pos_int_input(f'\tEnter score for quiz #{quiz + 1}: ')  # call to int validation function
        list_of_scores.append(quiz_score)

    return list_of_scores



def display(list_of_lists):
    total=0
    total_scores=0
    for index,list in enumerate(list_of_lists):
        total+=sum(list)
        total_scores+=len(list)
        print(f'the total for student# {index+1} is {sum(list)} and the average score is {sum(list)/len(list):.2f}')
    #print the grand total and averrage
    print(f'The total of all scores is {total} with a grand average of {total/total_scores:.2f}')

main()





