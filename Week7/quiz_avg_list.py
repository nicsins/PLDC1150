from library import inUtils as inu

def main():
    try:
        students=inu.posPutInt('please enter number of students')
        list_of_lists=get_scores(students)
        display(list_of_lists)
    except Exception as e:
        print(e)

def get_student_score(student):
    return [inu.putPosFloat(f'enter score for student #{student +1} quiz # {quiz+1}:') for quiz in range(inu.posPutInt(f"please enter the number of quizzes for student # {student +1}"))]

def get_scores(students):
    return [get_student_score(student)for student in range(students)]


def display(list_of_lists):
    total=0
    total_scores=0
    for index,list in enumerate(list_of_lists):
        total+=sum(list)
        total_scores+=len(list)

        print(f'the total for student# {index+1} is {sum(list)} and the average score is {sum(list)/len(list):.2f}')
    print(f'The total of all scores is {total} with a grand average of {total/total_scores:.2f}')



main()
