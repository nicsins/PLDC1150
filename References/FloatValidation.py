



def get_float(prompt):
    while True:
        try:
            flizzoat = float(input(prompt))
        except Exception as e:
            print(e)
            print("Must be a decimal number")
            continue
        if flizzoat<0:
            print('your float must be positive')
            continue
        else:
            break
    return flizzoat
if __name__ == '__main__':

  hourly_wage=get_float("please enter your hourly wage")

  print(f'you make ${hourly_wage:.2f} an hour')




# """first attempt  recursive example """
# def get_float():
#     while True:
#         try:
#             flizzoat = float(input("enter a positive float"))
#         except Exception as e:
#             print(e)
#             print("Must be a decimal number")
#             continue
#         else:
#             break
#     return flizzoat
#
# def is_pos_float():
#
#     flizzoat=get_float()
#     while flizzoat<0:
#         print('your float must be positive')
#         flizzoat = get_float()
#     return flizzoat


