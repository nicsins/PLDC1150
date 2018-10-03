'''Author = _name_
proigram calculates gross sales in a coffeee shop'''
#get user input
cupsCoffee=int(input('How many cups coffee'))
cupsTea=int(input('How many cups tea'))
cupsCap=int(input('How many cups cappuccino'))
costCoffee=float(input("how much per cup of Coffee"))
costTea=float(input("how much per cup of Tea"))
costCap=float(input("how much per cup of cappuccino"))

coffee_sales=cupsCoffee*costCoffee
tea_sales=cupsTea*costTea
cap_sales=cupsCap*costCap
total_sales=coffee_sales+tea_sales+cap_sales
print(f'the gross total sales  was ${total_sales:.2f}')
print('{:<20}{:<11}{:<6} {:<10}'.format("Drink Type","Cost","#drink","Tot/Drink"))
print("-"*50)
print(f'{"Coffee":.<20}${costCoffee:<10.2f}{cupsCoffee:<6}${coffee_sales:<10.2f}')
print(f'{"Tea":.<20}${costTea:<10.2f}{cupsTea:<6}${tea_sales:<10.2f}')
print(f'{"Cappuccino":.<20}${costCap:<10.2f}{cupsCap:<6}${cap_sales:<10.2f}')
print(f'the gross total sales  was ${total_sales:.2f}')

#
# print(f'{"Cups sold":.<21}{cups:>10d}')
# print(f'{"Cost per cup":.<20}${cost:>10.2f}')
# print(f'{"Total Sold":.<20}${coffee_sales:>10.2f}')
