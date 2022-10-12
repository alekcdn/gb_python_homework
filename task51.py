# 1. Напишите программу, удаляющую из текста все слова,
# содержащие ""абв"".

text = 'ИТ специалист  это представитель одной из более чем 500 цифровых профессий'
print(text)


def del_words(text):
    text = list(
        filter(lambda x: 'а' not in x and 'б' not in x and 'в' not in x, text.split()))
    return " ".join(text)


text1 = del_words(text)
print(text1)
