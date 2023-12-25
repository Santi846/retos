import secrets
# import string
import random

upperCaseLetters = "ABCDEFGHIJKLMNLOPQRSTUVWXYZ"

lowerCaseLetters = "abcefghijklmnopqrstuvwxyz"

numbers = "0123456789"

symbols = "!@#$%^&*"

password = ""

def generatePass(upper, lower, nums, syms, password):
    
    if upper:
        password += upper
        return password
    elif lower:
        password += lower
        return password
    elif nums:
        password += nums
        return password
    elif syms:
        password += syms
        return password
    
generatePass(upperCaseLetters, lowerCaseLetters, numbers, symbols, password)

def setLength(randomPassword):
    passwordLength = 16
    amounts = 8
    
    for i in range(amounts):
        randomPassword = "".join(random.sample(password, passwordLength))
        print(randomPassword)
        
setLength(generatePass())