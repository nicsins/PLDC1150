''' this program asks the user for the number of widgets they would like to buy then figures the discount using a conditional loop '''

#gloabl var
PRICE=99
# define main

def main():
    widgets=pos_int("how many widgets would you like to buy")
    discount=get_discount(widgets)
    retail_price, discounted_amount, total=calculate_items(widgets,discount)
    print_output(widgets, discount, retail_price, discounted_amount, total)


 #input validation using exception handling and conditional loop
def pos_int(prompt):
    while True:
        try:
            num=int(input(prompt))
        except ValueError:
            print(' Must be a valid whole number')
            continue
        if num<0:
            print('number must be greater than zero')
            continue
        else:
            break
    return num


# determine discount using conditional loop return value
def get_discount(widgets):
    if widgets > 99:
        discount = .4
    elif widgets > 49:
        discount = .3
    elif widgets > 19:
        discount = .2
    elif widgets > 10:
        discount = .1
    else:
        discount = 0
    return discount

def calculate_items(widgets,discount):

    retail_price=PRICE*widgets
    discounted_amount=retail_price*discount
    total=retail_price-discounted_amount
    return retail_price,discounted_amount,total
def print_output(widgets,discount,retail_price,discounted_amount,total):
    print(f'You are buying {widgets} widgets, earning a {discount:.2%} discount.')
    print(f'{"Retail price @99 each":25}${retail_price:>10,.2f}')
    print(f'{"Amount you saved today":25}${discounted_amount:>10,.2f}')
    print(f'{"Discount price b4 tax":25}${total:>10,.2f}')

if __name__ == '__main__':
    main()