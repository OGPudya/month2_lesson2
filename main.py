# текстовые, бинарные

# чтение - r(read)
# запись - w(write)
# дозапись - a(append)

# чтение rb(read bites)
# запись wb(write bites)


# open(путь_до_файл, режим работы, кодировка="utf-8") - открывает файл на указанный режим
# путь_до_файла
# абсолютный
# относительный

# file = open("byron.txt", mode="r", encoding="utf-8")
# .read() - считывает весь текст из файла
# .readlines() - считает каждую строку сформировав список строк
# .readline() - считывает каждую строку по очреди

# text = file.read()
# text = file.readlines()
# print(text)

# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readable())
# print(file.writable())
# file.close()

# запись данных в файл

# file2 = open('new_file.txt', mode="w", encoding="utf-8")
# .write() - записывает текст в одну строку
# .writelines(список_строк) - принимает список строк и записывает в файл
# file2.write('Hello world\n')
# file2.write('Привет мир')

# lines = [f'{i} строка\n' for i in range(1, 101)]
# file2.writelines(lines)
# file2.close()

# работа с бинарными файлами

# img = open('photo_2023-10-02_19-43-09.jpg', mode="rb")
# content = img.read()
# print(content)
# img.close()

# with - контекстный менеджер, позволяющий не закрывать соединение


# with open('photo_2023-10-02_19-43-09.jpg', mode="rb") as img:
#     content = img.read()
#     for i in range(1, 11):
#         new_img = open(f'{i}.jpg', mode='wb')
#         new_img.write(content)
#         new_img.close()
#
# print(img.closed)


file2 = open('new_file.txt', mode='a', encoding='utf-8')
lines = [f'{i} строка\n' for i in range(101, 201)]
file2.writelines(lines)
file2.close()