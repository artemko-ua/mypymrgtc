# 1. Змінні та типи даних
# Змінні - це "коробки", в яких зберігається інформація.

a = 1 # int - Цілі числа, наприклад, 1, 2, 100
b = 3.14 # float - Дробові числа, наприклад, 3.14, 2.718, 0.001
c = "Hello, World!" # str - Рядок (строка) тексту, наприклад, "Привіт", "Python"
d = True # bool - Логічні значення: True (істина) або False (хибність)
e = [1, 3.14, "text", True] # list - Список/масив, може містити елементи різних типів

# Як використовувати змінні
print(a) # Виведення значення змінної a на екран
print("Текст") # Виведення тексту на екран
print(a, "день літа") # Виведення комбінації змінної та тексту

# 2. Умови (if-elif-else)
# Іноді ми хочемо, щоб код виконувався тільки за певної умови.

age = 18

if age >= 18: # Якщо значення змінної age більше або дорівнює 18
    print("Ви повнолітній") # Виконується цей код
elif age > 12: # Інакше, якщо значення більше 12
    print("Ви підліток") # Виконується цей код
else: # Якщо жодна з попередніх умов не істинна
    print("Ви дитина") # Виконується цей код

# 3. Цикли (for, while)
# Цикли дозволяють виконувати код багато разів.

# Цикл while
counter = 0
while counter < 3: # Поки значення змінної counter менше 3
    print("Це цикл while. Counter =", counter)
    counter += 1 # Додаємо 1 до counter на кожному кроці

# Цикл for з діапазоном
for i in range(1, 4): # Цикл працює для значень i від 1 до 3 включно
    print("Це цикл for. Значення i =", i)

# Цикл for для списку
colors = ["червоний", "зелений", "синій"]
for color in colors: # Для кожного елемента списку colors
    print("Цей колір -", color)

# 4. Функції
# Функції дозволяють повторно використовувати код.

def greet(name): # Створення функції з параметром name
    return "Hello, " + name + "!" # Повертає строку з привітанням

# Виклик функції
message = greet("John") # Викликаємо функцію з параметром "John"
print(message) # Виводимо результат функції на екран

# 5. Словники (dict)
# Словники дозволяють зберігати пари "ключ-значення".

person = {
    "name": "Alice",
    "age": 25,
    "city": "London"
} # Створюємо словник з інформацією про людину

print(person["name"]) # Виводимо значення за ключем "name"
print(person["age"]) # Виводимо значення за ключем "age"

# 6. Обробка помилок (try-except)
# Код може містити помилки, і їх можна обробити за допомогою try-except.

try:
    number = int(input("Введіть число: ")) # Пробуємо перетворити введене значення на число
    print("Ваше число =", number)
except ValueError: # Якщо сталася помилка ValueError (введення не є числом)
    print("Це не число!") # Виконується цей код

# 7. Робота з файлами
# Ви можете читати з файлів і записувати в них інформацію.

# Запис у файл
with open("example.txt", "w") as file: # Відкриваємо файл для запису ("w")
    file.write("Це текст, записаний у файл.") # Записуємо текст у файл

# Читання з файлу
with open("example.txt", "r") as file: # Відкриваємо файл для читання ("r")
    content = file.read() # Читаємо весь вміст файлу
    print(content) # Виводимо вміст файлу на екран

# 8. Множинне присвоєння та розпакування списків
# Python дозволяє присвоювати значення кільком змінним одночасно.

x, y, z = 1, 2, 3 # Одночасно присвоюємо значення змінним x, y, z

# Розпакування списку
numbers = [4, 5, 6]
a, b, c = numbers # Розпаковуємо значення зі списку numbers у змінні a, b, c
print(a, b, c) # Виводимо значення змінних на екран

# 9. Вкладені структури даних
# Списки і словники можуть містити інші списки або словники.

nested_list = [1, [2, 3], [4, [5, 6]]] # Список всередині іншого списку
print(nested_list[1][1]) # Виводимо другий елемент внутрішнього списку [2, 3]

nested_dict = {
    "key1": {"subkey1": "value1"},
    "key2": {"subkey2": "value2"}
} # Словник всередині словника
print(nested_dict["key2"]["subkey2"]) # Виводимо значення за ключем "subkey2" словника "key2"

