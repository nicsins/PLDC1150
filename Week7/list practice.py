''' creates a loop that breaks when you hit enter'''
print('Type your guest\'s name, then hit enter.')
print('Hit enter again, when list is finished.')

guests=[]
while True:
    guest=input('guest name presss enter to quit')
    if guest=='':
         break
    guests.append(guest)
print(*guests,sep=',')
#Oops, didn't want that last guest

print(guests)
uninvited = guests.pop()
print('Name removed: ', uninvited)
print('Guest list: ', guests)


# add this code to program above
# prints list items with other info.
# treats last list item separately

for guest in guests:
	if guests.index(guest) < len(guests) -1:
		print(f'Guest #{guests.index(guest) + 1} is {guest}, ', end = "")
	else:
		print(f'and Guest # {guests.index(guest) + 1} is {guest}.')


''' how to total a list with a loop'''

rainfall = [0.8, 1.1, 1.3, 2.1, 0.6, 0.2, 7.6]
total_rain = 0
for rain in rainfall:
    total_rain += rain  # long form is total_rain = total_rain + rain
print('Total rain =', total_rain)

''' numbers cubes'''

print(lambda x :x**3 for x in [2,4,5,6,7,8,9])

'''ways to make lists'''
list()# turns something into a list... If possible

numbers = list(range(1,10))
print(numbers)

letters = list('Hennepin')
print(letters)

empty_list = list()
print(empty_list)

'''this crashes
numbers2 = list(7)
print(numbers2)
'''

''' using * and + in list '''
#Want a list of 100 zeros?
zeros = [0] * 100
print(zeros)

#Want to add all the items in one list to another list?
my_bands = ['Prince', 'Daft Punk', 'Led Zeppelin']
friends_bands = ['Lady Gaga', 'Rhianna', 'Beyonce']
roadtrip_playlist = my_bands + friends_bands
print(roadtrip_playlist )


#What happens if you remove element 1 from copy_of_data ? Does data change?

data = [7, 8, 9, 10]
copy_of_data = data[:]
copy_of_data.remove(8)
print(data)
print(copy_of_data )

#With a true copy of a list, changes to the original don't impact the copy and vice versa

data = [7, 8, 9, 10]
copy_of_data = data
data.remove(8)
print(data)
print(copy_of_data )
'''An alias is not an actual copy, just a reference to the same list ID as the original
Changes to the original are reflected in the alias, and vice versa
'''
