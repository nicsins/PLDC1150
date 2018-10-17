

'''a group of functions used to validate input data'''
import re


def putInt(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Value must be a whole number")
            continue
        else:
            break
    return value


def posPutInt(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Value must be a whole number")
            continue

        if value < 0:
            print("Sorry, your response must not be negative.")
            continue
        else:
            break
    return value


def putFloat(prompt):
    while True:
        try:
            flizzoat = float(input(prompt))
        except Exception as e:
            print(e)
            print("Must be a decimal number")
            continue
        else:
            break
    return flizzoat


def putPosFloat(prompt):
    while True:
        try:
            flizzoat = float(input(prompt))
        except Exception as e:
            print(e)
            print("Must be a decimal number")
            continue
        if flizzoat < 0:
            print('your float must be positive')
            continue
        else:
            break
    return flizzoat


def phone(prompt):
    while True:
       # Regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
        Regex=re.compile(r'^(\d{3})-(\d{3})-(\d{4})$') #found at https://www.bogotobogo.com/python/python_regularExpressions.php
        num=input(prompt)
        if Regex.fullmatch(num):
            break
        else:
            print('must be valid number xxx-xxx-xxxx')
            continue
    return num

def social(prompt):
    while True:
        Soc=re.compile(r'\d\d\d-\d\d-\d\d\d\d')
       # Soc=re.compile((r'^(\d{3})-(\d{3})-(\d{4})$'))
        num = input(prompt)
        if Soc.fullmatch(num):
            break
        else:
            print('must be valid number xxx-xx-xxxx')
            continue


    return num

def isIp(prompt):
    while True:
        ip=re.compile(r'(\d)|(\d\d)|(\d\d\d).(\d)|(\d\d)|(\d\d\d).(\d)|(\d\d)|(\d\d\d).(\d)|(\d\d)|(\d\d\d)')
        num = input(prompt)
        if ip.match(num):
            break
        else:
            print('must be valid ip address ')
            continue


    return num

def isEmail(prompt):
    while True:
        email=(r'[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}')
        num = input(prompt)
        if email.fullmatch(num):
            break
        else:
            print('must be valid email address name@email.com ')
            continue

    return num