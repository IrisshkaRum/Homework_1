# Список допустимых предметов для выбора
valid_items = ["меч", "лук", "топор", "щит", "зелье"]

# Функция для получения правильного ввода от авантюриста
def get_adventurer_choice():
    while True:
        # Получаем ввод от пользователя и разбиваем его на список
        user_input = input("Введите предметы через пробел: ").strip().split()
        
        # Проверяем, все ли введенные предметы допустимы
        if all(item in valid_items for item in user_input):
            return set(user_input)  # Возвращаем множество (удаляем дубликаты)
        else:
            # Если есть хотя бы один недопустимый предмет, выводим сообщение об ошибке
            print("Неверный предмет")

# Получаем выборы от трех авантюристов
adventurer1 = get_adventurer_choice()
adventurer2 = get_adventurer_choice()
adventurer3 = get_adventurer_choice()

# Находим пересечение (общие предметы) среди всех троих
common_items = adventurer1 & adventurer2 & adventurer3

# Выводим количество предметов, которые войдут в общий набор
print(len(common_items))

