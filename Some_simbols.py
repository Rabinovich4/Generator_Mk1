# import random


# def eng_alphabet(number_of_characters):
#     simbols = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#                 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
#                 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
#     random_string = ''.join(random.sample(simbols, number_of_characters))
#     return random_string
#
#
# user_input = int(input())
# result = eng_alphabet(user_input)
# print(result)


import random
import string


def generate_random_string(num):

    random_string = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=num))
    return random_string


# Пример использования функции
user_input = int(input("Введите число: "))
user_choise = int(input("Введите значение из 1/2/3/4: "))
result = generate_random_string(user_input)
print(result)
