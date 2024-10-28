# Список товаров с уникальными ID, именем и ценой
items = {
    "001": {"name": "Батончик", "price": 70},
    "002": {"name": "Вода", "price": 45},
    "003": {"name": "Газировка", "price": 64},
    "004": {"name": "Булочка", "price": 33},
}
# Функция для отображения списка товаров в формате таблицы
def show_items():
    print("| ID  | Название    | Цена |")
    print("|-----|-------------|------|")
    # Проходим по каждому товару в списке
    for item_id, item_info in items.items():
        # Выводим ID товара, его название и цену
        print(f"| {item_id} | {item_info['name']:<11} | {item_info['price']:>4} |")
# Основаная функция
def start_vending():
    # Отображаем список товаров
    show_items()
    # Запрашиваем у пользователя ID товара
    selected_id=input("Введите ID товара:").strip()
    # Если пользователь ввел "ОТМЕНА", завершить программу
    if selected_id=="ОТМЕНА":
        print("Программа завершена")
        return
    # Проверяем, существует ли товар с введенным ID
    if selected_id not in items:
        print("Такого товара не существует")
        return
    # Получаем цену выбранного товара
    item_price=items[selected_id]["price"]
    print(f"Для покупки внесите {item_price} тугриков")
    # Переменная для отслеживания внесенной суммы
    total_money_inserted=0
    # Пока сумма внесенных денег меньше цены товара
    while total_money_inserted<item_price:
        # Запрашиваем купюру
        user_input=input("Внесите купюру (10/50/100/500): ").strip()
        # Если ввод ОТМЕНА
        if user_input=="ОТМЕНА":
            print("Программа завершена")
            return
        # Ввод купюры
        bill_value=int(user_input)
            # Проверяем, является ли купюра допустимой
        if bill_value not in [10,50,100,500]:
            print("Недопустимая купюра")
        # Добавляем сумму купюры к общей сумме
        total_money_inserted+=bill_value
        # Если внесенная сумма больше или равна цене товара
        if total_money_inserted>=item_price:
            # Рассчитываем сдачу
            change=total_money_inserted-item_price
            print(f"Ваша сдача: {change} тугриков")
            return
        else:
            # Выводим, сколько осталось внести
            remaining_amount=item_price-total_money_inserted
            print(f"Осталось внести {remaining_amount} тугриков")
start_vending()
