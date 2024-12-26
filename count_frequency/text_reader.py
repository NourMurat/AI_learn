# Открываем файл для чтения
with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()  # Читаем весь текст из файла

# Выводим текст на экран
print("Содержимое файла:")
print(text)
