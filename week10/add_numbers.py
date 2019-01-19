

def get_input():
    while True:
        try:
            nums= input('please enter a series of 5 numbers')
        except ValueError:
            print('must be all numbers')
            continue
        if nums.isdigit is False or len([d for d in nums])!=5 :
           print('must be a group of numbers no greater than 99999 and only numbers')
           continue
        else:
           break

    return [int(d) for d in nums]



def print_output(Map):
    for num in Map:
        if num != Map[len(Map)-1]:
            print(num, "+ ", end='')
        else:
            print(num, "= ", end='')
    print(sum(Map))



if __name__ == '__main__':
    Map=get_input()
    print_output(Map)



