import random
import string
from tkinter import *
from tkinter import ttk
import pyperclip


root = Tk()
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

btn_simbols = ttk.Radiobutton(text='Спец-символы', value=simbols)
btn_simbols.pack()

btn_digits = ttk.Radiobutton(text='Цифры', value=digits)
btn_digits.pack()

btn_alphabet = ttk.Radiobutton(text='eng.буквы', value=alphabet)
btn_alphabet.pack()

btn_all_simbols = ttk.Radiobutton(text='Всё подряд', value=all_simbols)
btn_all_simbols.pack()

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
    else:
        selected_button = None


# Вызов функции check_selection() для проверки выбранной кнопки
check_selection()

# В переменной selected_button будет содержаться название выбранной кнопки,
# либо None, если ни одна кнопка не выбрана


def choice(user_num, data_type):
    znaki = ''.join(random.choices(data_type, k=user_num))
    return znaki


def generate_simbols():
    user_input = int(entry.get())
    check_selection()  # Обновляем значение selected_button
    data_type = simbols if selected_button == 'Спец-символы' else \
        digits if selected_button == 'Цифры' else \
            alphabet if selected_button == 'eng.буквы' else \
                all_simbols if selected_button == 'Всё подряд' else None

    if data_type is not None:
        result = choice(user_input, data_type)
        label.config(text=result)
        pyperclip.copy(result)
    else:
        label.config(text='Выберите тип данных')


btn_start_choice = ttk.Button(text='Сгенерировать', command=generate_simbols)
btn_start_choice.pack()


root.mainloop()  # Последняя строка кода
