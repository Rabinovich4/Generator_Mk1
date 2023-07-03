import random
import string
from tkinter import *


simbols = ''.join(string.punctuation)
digits = ''.join(string.digits)
alphabet = ''.join(string.ascii_letters)
all_simbols = ''.join(string.punctuation + string.digits + string.ascii_letters)


def type_data(user_data_type):
    if user_data_type == '1':
        data_type = simbols
    elif user_data_type == '2':
        data_type = digits
    elif user_data_type == '3':
        data_type = alphabet
    else:
        data_type = all_simbols
    go_to_next_function = data_type
    return go_to_next_function


def choise(user_num, go_to_next_function):
    for i in range(user_num):
        znaki = ''.join(random.choices(go_to_next_function, k=user_num))
        return znaki


# Пример использования функции
user_input = int(input("Введите число: "))
user_data_input = type_data(input("Введите значение из 1/2/3/4: "))
result = choise(user_input, user_data_input)
print(result)
