# Сначала запрашиваем количество ходов N
N=int(input("Введите N:"))
# Изначально Пётр находится в точке (0, 0)
x = 0  # Координата по оси x
y = 0  # Координата по оси y
# Обрабатываем N ходов
for i in range(1,N+1):
    direction = input(f"Ход {i}:").strip().lower()
    # В зависимости от направления изменяем координаты
    if direction=="вверх":
        y+=1  # Вверх увеличивает координату y
    elif direction=="вниз":
        y-=1  # Вниз уменьшает координату y
    elif direction=="вправо":
        x+=1  # Вправо увеличивает координату x
    elif direction=="влево":
        x-=1  # Влево уменьшает координату x
    else:
        print("Некорректное направление, попробуйте снова")
        break
# Кратчайшее расстояние до конечной точки равно сумме абсолютных значений координат x и y
shortest_distance=abs(x)+abs(y)
print(shortest_distance)
