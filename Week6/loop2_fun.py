from library import inUtils as inu


def get_small():
    return inu.posPutInt('enter a small number')

def get_big(small):
    while True:
        big=inu.posPutInt('enter a larger number')
        if big < small:
            print('must be larger than your first number')
            continue
        else:
            break
    return big

def print_numbers(small,big):
    sum=0
    for num in range(small, big + 1):
        if num != big:
            print(num, "+", end='')
        else:
            print(num, "= ", end='')
        sum += num
    print(sum)

if __name__ == '__main__':
    small=get_small()
    big=get_big(small)
    print_numbers(small, big)


