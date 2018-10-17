'''this rogram shows how to add things to lists
this rogram records the number of hits in each
 round while some friends are shooting clay pigeons
 in a contest'''

def main():

    people=pos_int('How many people enter the contest')
    rounds=pos_int('How many rounds did each person shoot?')
    get_all_shooters_stats(people, rounds)



def get_scores(rounds):
    return [ pos_int(f'how many hits in round { i +1}') for i in range(rounds)]



def get_all_shooters_stats(people,rounds):

    list_of_scoreLists=[]
    avgList=[]
    for person in range (people):
        print(f' For student # {person+1}')
        hitList=get_scores(rounds)
        list_of_scoreLists.append(hitList)
        average=print_avg(person,hitList)
        avgList.append(average)
    total_of_each_student=get_total(list_of_scoreLists)
    display_stuff(total_of_each_student, avgList)


def get_total(list_of_scoreLists):

    total_of_each_student=[]
    for hit_list in list_of_scoreLists:
        total_of_each_student.append(sum(hit_list))

    return total_of_each_student

def print_avg(person,hitList):
    average=sum(hitList)/len(hitList)
    print(f' The average number of hits per attempt out of {len(hitList)}\n'
          f' for shooter #{person+1} if {average}')
    return average


def display_stuff(total_of_each_student,avgList):
    print(total_of_each_student)
    print(f'the total of scores together is {sum(total_of_each_student)}')
    print(f'the average score for everyone is {sum(avgList)/len(avgList)}')


def pos_int(prompt):
    while True:
        try:
            num=int(input(prompt))
        except ValueError:
            print(('must be a real number'))
            continue
        if num < 0:
            print('num must be grater than 0')
        else:
            break
    return num


main()