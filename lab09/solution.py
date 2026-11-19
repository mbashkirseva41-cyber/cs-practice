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


