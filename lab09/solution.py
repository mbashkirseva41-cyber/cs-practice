import numpy as np


def make_hours():
    # Создаёт массив [0, 3, 6, 9, 12, 15, 18, 21] и преобразует его в обычный список
    return np.arange(0, 22, 3).tolist()


def vector_report(values):
    # Превращаем входной список в массив NumPy с типом float (как в примере вывода)
    arr = np.asarray(values, dtype=float)
    
    return {
        "third": float(arr[2]),              # третий элемент (индекс 2)
        "last": float(arr[-1]),              # последний элемент
        "middle": arr[2:6].tolist(),         # срез с 2 по 5 индекс включительно
        "every_second": arr[::2].tolist(),   # каждый второй элемент
        "reversed": arr[::-1].tolist()       # развёрнутый вектор
    }


def change_vector(values):
    # Создаём независимую копию массива, чтобы не менять исходные данные
    arr = np.asarray(values).copy()
    arr[2:5] = 99    # заменяем элементы с индексами 2, 3, 4 на 99
    arr[::2] = -1    # заменяем каждый второй элемент на -1
    return arr.tolist()


def cap_above(values, limit):
    # Создаём копию массива
    arr = np.asarray(values).copy()
    # Логическая маска: находим все элементы больше limit и заменяем их на limit
    arr[arr > limit] = limit
    return arr.tolist()


def celsius_to_fahrenheit(values):
    arr = np.asarray(values, dtype=float)
    # Векторизованное вычисление сразу для всего массива без циклов
    fahrenheit = arr * 9 / 5 + 32
    return fahrenheit.tolist()
