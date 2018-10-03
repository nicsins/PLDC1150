name1=input("Please enter your name")
print(f'Hello {name1} !')
# print(f'Hello {input("Please enter your name")} !')# one liner

num_cd =int(input("number of cds?"))
num_lps =int(input("number of lps?"))
num_abm =num_cd + num_lps
print(f'you have {num_cd} CDs and {num_lps} lps \n  your total number of albums is {num_abm}')
print('you have',num_cd,'cd and',num_lps,'alblums')



import time,datetime
t= time.ctime()
f = datetime.datetime.strptime(t, '%a %b %d %H:%M:%S %Y')
print (f)
