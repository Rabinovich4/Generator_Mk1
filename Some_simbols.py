import random
import string
from tkinter import *
from tkinter import ttk
import pyperclip

root = Tk()     # начало окнта ткинтера
root.title('Generator_Mk1')
root.geometry('500x500')

entry = ttk.Entry(root)
entry.pack()

label = Label(text='Это метка, братан.')
label.pack()

simbols = ''.join(string.punctuation)
digits = ''.join(string.digits)
alphabet = ''.join(string.ascii_letters)
all_simbols = ''.join(string.punctuation + string.digits + string.ascii_letters)
phone_number_8 = '1'.join(string.digits)    # почему-то выбирается все три кнпки если убрать цифры из ковычекк телефонов
phone_number_plus_7 = '2'.join(string.digits)

btn_simbols = ttk.Radiobutton(text='Спец-символы', value=simbols)
btn_simbols.pack()

btn_digits = ttk.Radiobutton(text='Цифры', value=digits)
btn_digits.pack()

btn_alphabet = ttk.Radiobutton(text='eng.буквы', value=alphabet)
btn_alphabet.pack()

btn_all_simbols = ttk.Radiobutton(text='Всё подряд', value=all_simbols)
btn_all_simbols.pack()

btn_phone_number_8 = ttk.Radiobutton(text='Телефон с 8...', value=phone_number_8)
btn_phone_number_8.pack()

btn_phone_number_plus_7 = ttk.Radiobutton(text='Телефон с +7...', value=phone_number_plus_7)
btn_phone_number_plus_7.pack()

selected_button = None


def check_selection():
    global selected_button
    if btn_simbols.state() == ('selected',):
        selected_button = 'Спец-символы'
    elif btn_digits.state() == ('selected',):
        selected_button = 'Цифры'
    elif btn_alphabet.state() == ('selected',):
        selected_button = 'eng.буквы'
    elif btn_all_simbols.state() == ('selected',):
        selected_button = 'Всё подряд'
    elif btn_phone_number_8.state() == ('selected',):
        selected_button = 'Телефон с 8...'
    elif btn_phone_number_plus_7.state() == ('selected',):
        selected_button = 'Телефон с +7...'
    else:
        selected_button = None


# Вызов функции check_selection() для проверки выбранной кнопки (ОНО ВООБЩЕ НАДО?!)
check_selection()


# В переменной selected_button будет содержаться название выбранной кнопки,
# либо None, если ни одна кнопка не выбрана

def choice(user_num, data_type):
    if selected_button in {'Телефон с +7...', 'Телефон с 8...', }:
        if selected_button == 'Телефон с +7...':
            znaki = ''.join(random.choices(data_type, k=10))
            return f"+7{znaki}"
        else:
            znaki = ''.join(random.choices(data_type, k=10))
            return f"8{znaki}"
    else:
        znaki = ''.join(random.choices(data_type, k=user_num))
        return znaki


def generate_simbols():
    user_input = entry.get()
    if user_input == '':
        user_input = 10
    else:
        user_input = int(user_input)
    check_selection()  # Обновляем значение selected_button
    data_type = simbols if selected_button == 'Спец-символы' else \
        digits if selected_button == 'Цифры' else \
            alphabet if selected_button == 'eng.буквы' else \
                all_simbols if selected_button == 'Всё подряд' else \
                    digits if selected_button == 'Телефон с 8...' else \
                        digits if selected_button == 'Телефон с +7...' else None

    if data_type is not None:
        result = choice(user_input, data_type)
        label.config(text=result)
        pyperclip.copy(result)
    else:
        label.config(text='Выберите тип данных')


btn_start_choice = ttk.Button(text='Сгенерировать', command=generate_simbols)
btn_start_choice.pack()

root.mainloop()  # конец окна ткинтера
