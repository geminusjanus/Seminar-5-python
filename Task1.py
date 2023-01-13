# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


with open("Task1.txt", "r", encoding='utf-8') as file1:
    txt = file1.readline()
find_txt = "абв"
lst = [i for i in txt.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')