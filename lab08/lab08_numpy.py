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

##Задание 4. Прямоугольные срезы
print("\n--- Задание 4 ---")
matrix = np.arange(1, 26).reshape(5, 5)##матрица размером 5на5, числа от 1 до 25
part1 = matrix[ :3 ]
print("Первые три строки:\n", part1, "\nshape:", part1.shape)
part2 = matrix[ -2: ]
print("Последние две строки:\n", part2, "\nshape:", part2.shape)
part3 = matrix[ :, :2 ]
print("Первые два столбца:\n", part3, "\nshape:", part3.shape)
part4 = matrix[ 1:4, 2:5 ]
print("Строки 1–3, столбцы 2–4:\n", part4, "\nshape:", part4.shape)
part5 = matrix[ -2:, -2: ]
print("Угловой блок 2x2 в правом нижнем углу:\n", part5, "\nshape:", part5.shape)
##np.arange(1,26) создает одномерный список от 1 до 25
##.reshape(5,5) перестраивает эти 25 чисел в таблицу из 5i 5j

##Задание 5. Изменение массива с помощью срезов
print("\n--- Задание 5 ---")
vector = np.array([ 10, 20, 30, 40, 50 ])
vector[ 1:4 ] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[ 0, : ] = -1
small_matrix[ 1:, 1: ] = 9

changed_hours = hours.copy()
##независимая копия вектора h эл-ты с 2 по 4 меняются на 99
##
changed_hours[ 2:5 ] = 99
changed_hours[ ::2 ] = -1

print("changed_hours:", changed_hours)
print("Исходный hours:", hours)
# .copy() создаёт независимую копию данных в памяти.
# Без .copy() изменения в changed_hours изменили бы и исходный массив hours.

changed_matrix = matrix.copy()
changed_matrix[ 1, : ] = 0
changed_matrix[ :, -1 ] = -1
changed_matrix[ 1:4, 1:4 ] = 100
print("Итоговая changed_matrix:\n", changed_matrix)
print("Исходная matrix:\n", matrix)