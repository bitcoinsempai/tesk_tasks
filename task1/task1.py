import sys

def circular_array(n, m):
    # Круговой массив от 1 до n
    nums_arr = list(range(1, n + 1))
    path = []  # Список для хранения пути
    index = 0  # Текущий индекс, начинаем с 0

    # Добавляем первый элемент в путь
    path.append(nums_arr[index])

    # цикл работает, пока следующий индекс не вернёт нас к началу
    while (index + m - 1) % n != 0:
        # Вычисляем следующий индекс
        index = (index + m - 1) % n
        path.append(nums_arr[index])

    return ''.join(map(str, path))

# Получаем аргументы командной строки
if len(sys.argv) == 3:
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    # Выводим результат
    print(circular_array(n, m))
else:
    print("Please provide two arguments: n (size of the array) and m (step interval).")