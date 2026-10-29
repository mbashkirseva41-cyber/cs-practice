import numpy as np

def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if len(values) % width != 0:
        return []
    arr = np.asarray(values)
    reshaped = arr.reshape(-1, width)
    return reshaped.tolist()

def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:
    arr = np.asarray(matrix)
    sub_matrix = arr[np.ix_(rows, columns)]
    return sub_matrix.tolist()

def column_means(matrix: list[list[float]]) -> list[float]:
    if not matrix or len(matrix) == 0:
        return []
    arr = np.asarray(matrix)
    means = arr.mean(axis=0).round(6)
    return means.tolist()

def column_range(matrix: list[list[float]], column: int) -> float:
    if not matrix or len(matrix) == 0:
        return 0.0
    arr = np.asarray(matrix)
    col_data = arr[:, column]
    res = (col_data.max() - col_data.min()).round(6)
    return float(res)
#финальная версия для проверки