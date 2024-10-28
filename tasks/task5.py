# Список допустимых предметов для выбора
valid_items=["меч","лук","топор","щит","зелье"]
# Функция для получения правильного ввода от авантюриста
def get_adventurer_choice():
    while True:
        # Получаем ввод и разбиваем на список
        user_input=input("Введите предметы через пробел:").split()
        # Проверяем
        if all(item in valid_items for item in user_input):
            return set(user_input)  # Возвращаем множество (удаляем дубликаты)
        else:
            # Если неверный ввод
            print("Неверный предмет")
# Получаем выборы от трех авантюристов
adventurer1=get_adventurer_choice()
adventurer2=get_adventurer_choice()
adventurer3=get_adventurer_choice()
# Находим пересечение среди всех троих
common_items=adventurer1&adventurer2&adventurer3
print(len(common_items))

