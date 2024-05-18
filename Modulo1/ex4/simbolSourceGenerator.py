import random
import os

from FontAssociatedWithRange import fontAssociatedWithRange
from Utils import show_symbols_info, write_sequence_to_file, delete_file

alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upperAlfabet = [letter.upper() for letter in alfabet]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbolsList = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']

def repeat_code(num, code):
    for i in range(num):
        print(code())
    print("\n")

def generate_symbols(number_of_symbols, alfabetToUse=alfabet, showInfo=False):
    symbolsRange = fontAssociatedWithRange(alfabetToUse, showInfo)
    finalSimbol = ''
    while len(finalSimbol) < number_of_symbols:
        result = symbolsRange.getSimbolByRange(random.random())
        if result:
            finalSimbol += result
    return finalSimbol


def generate_symbols_test(num, filename, alabetToUse=alfabet, showInfo=False, deleteFile=True):
    sequence = generate_symbols(num, alabetToUse, showInfo)
    write_sequence_to_file(filename, sequence)
    current_directory = os.getcwd()
    if showInfo:
        show_symbols_info(filename, current_directory)
    if deleteFile:
        delete_file(filename)
    return sequence


generate_symbols_test(5, "symbols.txt", ['a', 'a', 'a', 'b', 'b'], True)

repeat_code(10, lambda: generate_symbols_test(5, "symbols.txt", ['a', 'a', 'a', 'b', 'b']))

print(generate_symbols_test(4, "password.txt", ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], True))
print("\n")
print(generate_symbols_test(6, "password.txt", ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], True))
print("\n")

repeat_code(10, lambda: generate_symbols_test(4, "password.txt", ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']))
repeat_code(10, lambda: generate_symbols_test(6, "password.txt", ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']))


def generate_euromilhoes_key():
    numbers = []
    stars = []
    symbolsRange = fontAssociatedWithRange([str(i) for i in range(1, 51)])
    while len(numbers) < 5:
        number = int(symbolsRange.getSimbolByRange(random.random()))
        if number: 
            if number not in numbers:
                numbers.append(number)
    symbolsRange = fontAssociatedWithRange([str(i) for i in range(1, 13)])
    while len(stars) < 2:
        star = int(symbolsRange.getSimbolByRange(random.random()))
        if star: 
            if star not in stars:
                stars.append(star)
    return {"numbers": numbers, "stars": stars}

repeat_code(10, generate_euromilhoes_key)


def password_generator(length): 
    symbolsRange = fontAssociatedWithRange(alfabet+ numbers + symbolsList + upperAlfabet)
    password = ''
    while len(password) < length:
        result = symbolsRange.getSimbolByRange(random.random())
        if result:
            password += result
    digitCondition = any(char.isdigit() for char in password)
    lowerCondition = any(char.islower() for char in password)
    upperCondition = any(char.isupper() for char in password)
    symbolCondition = any(char in symbolsList for char in password)
    if not (digitCondition and lowerCondition and upperCondition and symbolCondition):
        return password_generator(length)
    return password

repeat_code(10, lambda: password_generator(8))

for i in range(8, 13):
    print(password_generator(i))

# file with 1000 passwords
passswordFile = "passwords.txt"
passwords = ""
for i in range(1000):
    if (i != 999):
        passwords += password_generator(8) + "\n"
    else:
        passwords += password_generator(8)
write_sequence_to_file(passswordFile, passwords)