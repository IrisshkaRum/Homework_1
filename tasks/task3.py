person = ['Энакин Скайуокер', 
          41, 
          ['Татуин', 'Набу', 'Джеонозис', 'Корусант', 'Мустафар', 'Звезда Смерти'], 
          {'световой меч': 'синий', 'ранг': 'лорд ситхов'}
          ]
# Функция, которая обрабатывает выбор пользователя
def handle_choice(choice):
    # 1. Вывести фамилию и имя
    if choice==1:
        # Разделяем строку имени на две части - фамилия и имя
        last_name,first_name=person[0].split()
        print(f"Персона: {last_name},{first_name}")
    # 2. Вывести возраст
    elif choice==2:
        print(f"Возраст: {person[1]}")
    # 3. Вывести все места через запятую
    elif choice==3:
        places=", ".join(person[2])
        print(f"Места: {places}")
    # 4. Найти и вывести количество мест
    elif choice==4:
        number_of_places=len(person[2])
        print(f"Количество мест: {number_of_places}")
    # 5. Проверить, служил ли он на Звезде Смерти
    elif choice==5:
        serves_empire = 'Звезда Смерти' in person[2]
        print(serves_empire)
    # 6. Напечатать цвет светового меча
    elif choice==6:
        print(f"Цвет светового меча: {person[3]['световой меч']}")
    # 7. Изменить возраст Энакина на 42 и вывести его
    elif choice==7:
        person[1] = 42
        print(f"Новый возраст: {person[1]}")
    # 8. Добавить новое место 'Эндор' в список, если его там нет
    elif choice==8:
        if 'Эндор' not in person[2]:
            person[2].append('Эндор')
        print(f"Обновленный список мест: {person[2]}")
    # 9. Проверить ранг и вывести сообщение
    elif choice==9:
        if person[3]['ранг']=='лорд ситхов':
            print("Энакин - лорд ситхов")
        else:
            print("Энакин - джедай")
    # 10. Проверить количество посещенных мест
    elif choice==10:
        if len(person[2])>4:
            print("Энакин побывал во многих местах")
        else:
            print("Энакин не так много путешествовал")
# Основной цикл
while True:
    # Запрашиваем команду
    user_input=input("Введите номер задания (или 'выход' для завершения):").strip()
    # Если пользователь вводит "выход", программа завершается
    if user_input.lower()=="выход":
        print("Программа завершена")
        break
    task_number=int(user_input)
    # Проверяем, что введенный номер задания находится в диапазоне от 1 до 10
    if 1<=task_number<=10:
        # Обрабатываем введенный номер задания
        handle_choice(task_number)
    else:
        print("Введите число от 1 до 10")
