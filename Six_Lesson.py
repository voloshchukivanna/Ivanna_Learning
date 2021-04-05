

# f = open('ivankasong.txt', 'r)
# print(f.read())
# f.close()


# f = open('ivankasong.txt', 'r')
# x = f.read()
# print(x)

# with open('lalala.txt') as f:
#     f.read()

'''Задание: считываем построчно строки из файла и выводим строки,
добавляя в конец этих строк восклицательный знак'''

# f = open('ivankasong.txt')
# for line in f:
#     print(line.rstrip() + "!")
# f.close()

'''Записываем “Number: строка из файла” из одного файла в другой. Не 
забываем закрывать файлы'''

# with open('ivankasong.txt', 'r') as f, open('ivankasecond.txt', 'w') as f1:
#     for idx, line in enumerate(f, start=1):
#         f1.write('{} {}'. format(idx, line))

'''Напишите программу, которая пытается преобразовать текст из файла в 
число. Файл должен все равно закрываться в блоке finally. Если 
преобразование удалось (в блоке else) – выводится сообщение «I did it!»'''

f = open('ivankasecond.txt')
ints = []
try:
    for line in f:
        ints.append(int(line))
except ValueError:
    print("Это не число")
except Exception:
    print('Это что ещё такое?')
else:
    print("I did it!")
finally:
    f.close()
    print("Closing files!")
