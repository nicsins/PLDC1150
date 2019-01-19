'''this program asks the user for a monthly budget'''
#define global var
UTILITIES=["Rent","Food","Transport","Other"]

def get_costs():
    return [pos_float(f'enter cost for {item}') for item in UTILITIES]


def display_output(costs):
    print("Here's your overall budget:")
    print('{:<20}{:<20}{:<20}{:<20}'.format(*UTILITIES))

    print('${:<19,.2f}${:<19,.2f}${:<19,.2f}${:<19,.2f}'.format(*costs))
    print(f'\nYour total monthly budget is ${sum(costs):,.2f}')


def pos_float(prompt): # input validation using exception handling and conditional loop
    while True:
        try:
            num = float(input(prompt))
        except ValueError:
            print(' Must be a valid whole number')
            continue
        if num < 0:
            print('number must be greater than zero')
            continue
        else:
            break
    return num


if __name__ == '__main__':
    try:
        costs=get_costs()
        display_output(costs)
    except Exception as e:
        print(e)
