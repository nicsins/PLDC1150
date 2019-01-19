''' Mouhari Mouhamed 10-18-19  "Personal budget."  This program
will help the user put together a personal budget by gathering data
on user rent, food , transportation other expenses. '''

print("Welcome to the personal budget program!")
#def budget(): this needes to be called main thats just how it works
def main():
    rentPrice = expenseOnRent()
    totalRentexpense(rentPrice)
    foodPrice = expenseOnfood()
    totatFoodexpense(foodPrice)
    transportPrice = expenseOntransport()
    totatTransportexpense(transportPrice)
    priceOfother = otherExpense()
    totatOtherexpense(priceOfother)





def expenseOnRent():
    print("How much do you spend for Rent?")
    rentPrice = float(input('\tEnter a positive whole number: '))
    return rentPrice

def totalRentexpense(rentPrice):
    totalRent = 0
    totalRent = totalRent+ rentPrice
    return totalRent

def expenseOnfood():
    print("How much do you spend for Food?")
    foodPrice= float(input("Enter a positive whole number: "))
    return foodPrice
def totatFoodexpense(foodPrice):
    totalFood=0
    totalFood=totalFood+ foodPrice
    return totalFood

def expenseOntransport():
    print("How much do you spend for Transport?")
    transportPrice= float(input("Enter a positive whole number: "))
    return transportPrice
def totatTransportexpense(transportPrice):
    totalTransport=0
    totalTransport=totalTransport + transportPrice
    return totalTransport

def otherExpense():
    print("How much do you spend for Other?")
    priceOfother= float(input("Enter a positive whole number: "))
    return priceOfother
def totatOtherexpense(priceOfother):
    otherTotal=0
    otherTotal=otherTotal + priceOfother
    return otherTotal

def overal_budget(totalRent, totalFood, totalTransport, otherTotal):
    list.append(totalRent, totalFood, totalTransport, otherTotal)
    print(totalRent, totalFood, totalTransport, otherTotal)

main()