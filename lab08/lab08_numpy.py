import numpy as np
#задание 1. Создание векторов и матриц
print('\n---Задание 1---')
hours = np.arange(0,22,3)
line = np.linspace(0,1,5);
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2,3),-1)
identity = np.eye(3)

print('hours: ', hours)
print('shape:', hours.shape, "ndim:", hours.ndim, "size:", hours.size, "dtype:", hours.dtype )

# Задание 2. Индексы и срезы в векторе
print("\n--- Задание 2 ---")
print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2–5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("В обратном порядке:", hours[::-1])

# Задание 3. строки и столбцы таблицы
print("\n--- Задание 3 ---")
temperatures = np.array([
    [ 12, 14, 13, 15 ],
    [ 11, 13, 16, 17 ],
    [ 10, 12, 15, 18 ],
])
print("Форма:",temperatures.shape, "Измерений:", temperatures.ndim, "Элементов:", temperatures.size )
print("Вторая строка, третий столбец:", temperatures[1,2])
print("Первая строка: ", temperatures[0])
print("Последний столбец: ", temperatures[:,-1])##[строки, столбцы]
print("Первые две строки без первого столбца:\n", temperatures[ :2, 1: ])
##\n - enter
center = temperatures[0:2, 1:3]
print("2*2: \n", center)
print("форма центрального фрагмента: ", center.shape)

