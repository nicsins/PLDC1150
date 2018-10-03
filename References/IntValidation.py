def get_pos_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if value < 0:
            print("Sorry, your response must not be negative.")
            continue
        else:
            break
    return value

if __name__ == '__main__':
    age=get_pos_int("please enter your age")
    kids=get_pos_int("please enter how many kids")