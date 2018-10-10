def main():
    small=pos_int_input("enter a small number")
    big=get_big(small)
    total=processing(small,big)
    print_Output(total)



def get_big(small):
    while True:
        big=pos_int_input('enter a larger number')
        if big<small:
            print("number must be larger than the first")
            continue
        else:
            break
    return big

def processing(small,big):
    total=[]
    for num in range(small,big+1):
        if num != big:
            print(num, "+", end='')
        else:
            print(num, "=", end='')
        total.append(num)
    print(sum(total))

    return total

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



def print_Output(total):
    print(*total,sep=',')
    print(f'the total sum of the numbers is {sum(total)}')

if __name__ == '__main__':
    main()