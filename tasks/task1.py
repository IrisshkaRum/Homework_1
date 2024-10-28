# Запрашиваем ввод
variable_name=input("имя переменной:")
# Основная функция
def correct_variable_name(variable_name):
    # Заменяем - на _
    variable_name = variable_name.replace("-","_")
    # Заменяем пробелы на _"
    variable_name = variable_name.replace(" ","_")
    # Вспомогательная строка
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Превращаем строку в список для удобства
    variable_name_list=list(variable_name)
    # Проходим по каждому символу
    for i in range(len(variable_name_list)):
        if variable_name_list[i] in upper:
            # Добавляем перед заглавной буквой _ и заменяем её на строчную
            variable_name_list[i]="_"+variable_name[i].lower()
    # Возвращаем строку
    variable_name="".join(variable_name_list)
    # Заменяем __ на _
    while "__" in variable_name:
        variable_name = variable_name.replace("__","_")
    # Удаляем пробелы, подчеркивания и цифры в начале имени переменной
    while variable_name[0]==" " or variable_name[0]=="_" or variable_name[0].isdigit():
        variable_name=variable_name[1:]
    # Удаляем пробелы в конце имени переменной
    while variable_name[-1]==" ":
        variable_name=variable_name[:-1]
    # Допустимые символы для имени переменной
    symbols = "abcdefghijklmnopqrstuvwxyz0123456789_"
    # Проверяем
    for symbol in variable_name:
        if symbol not in symbols:
            # Если встречается недопустимый символ
            return "некорректное имя переменной"
    return variable_name
print(correct_variable_name(variable_name))
