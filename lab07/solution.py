import numpy as np

def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if not values or width <= 0 or len(values) % width != 0:
        return []
    arr = np.asarray(values, dtype=float)
    return arr.reshape(-1, width).tolist()


def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:
    if not matrix or not rows or not columns:
        return []
    arr = np.asarray(matrix, dtype=float)
    sub_arr = arr[np.ix_(rows, columns)]
    return sub_arr.tolist()


def column_means(matrix: list[list[float]]) -> list[float]:
    if not matrix:
        return []
    arr = np.asarray(matrix, dtype=float)
    means = np.mean(arr, axis=0)
    return [round(float(x), 6) for x in means]


def column_range(matrix: list[list[float]], column: int) -> float:
    if not matrix:
        return 0.0
    arr = np.asarray(matrix, dtype=float)
    col_data = arr[:, column]
    val_range = np.ptp(col_data) 
    return round(float(val_range), 6)