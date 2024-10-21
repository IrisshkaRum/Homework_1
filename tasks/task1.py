# Запрашиваем у пользователя ввод имени переменной
variable_name = input("имя переменной: ")

# Функция для корректировки имени переменной
def correct_variable_name(variable_name):
    # Заменяем все символы "-" на "_"
    variable_name = variable_name.replace("-", "_")
    
    # Заменяем все пробелы на "_" 
    variable_name = variable_name.replace(" ", "_")

    # Определяем строку с заглавными буквами
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Превращаем строку переменной в список для удобства изменения символов
    variable_name_list = list(variable_name)
    
    # Проходим по каждому символу в списке
    for i in range(len(variable_name_list)):
        # Если символ является заглавной буквой
        if variable_name_list[i] in upper:
            # Добавляем перед заглавной буквой "_" и заменяем её на строчную
            variable_name_list[i] = "_" + variable_name[i].lower()

    # Собираем обратно строку из списка символов
    variable_name = "".join(variable_name_list)

    # Удаляем возможные двойные символы "__", заменяя их на один "_"
    while "__" in variable_name:
        variable_name = variable_name.replace("__", "_")
    
    # Удаляем пробелы, подчеркивания и цифры в начале имени переменной
    while variable_name[0] == " " or variable_name[0] == "_" or variable_name[0].isdigit():
        variable_name = variable_name[1:]
    
    # Удаляем пробелы в конце имени переменной
    while variable_name[-1] == " ":
        variable_name = variable_name[:-1]

    # Допустимые символы для имени переменной: строчные буквы английского алфавита, цифры и "_"
    symbols = "abcdefghijklmnopqrstuvwxyz0123456789_"
    
    # Проверяем, что все символы в имени переменной допустимы
    for symbol in variable_name:
        if symbol not in symbols:
            # Если встречается недопустимый символ, возвращаем сообщение об ошибке
            return "некорректное имя переменной"

    # Возвращаем скорректированное имя переменной
    return variable_name

# Выводим результат корректировки имени переменной
print(correct_variable_name(variable_name))
