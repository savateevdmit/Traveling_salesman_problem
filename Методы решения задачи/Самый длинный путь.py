import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from python_tsp.exact import solve_tsp_dynamic_programming
from scipy.spatial import distance_matrix

# Функция нахождения минимального элемента, исключая текущий элемент
def Min(lst, myindex):
    return min(x for idx, x in enumerate(lst) if idx != myindex)


# функция удаления нужной строки и столбцах
def Delete(matrix, index1, index2):
    del matrix[index1]
    for i in matrix:
        del i[index2]
    return matrix


# Функция вывода матрицы
def PrintMatrix(matrix):
    print("---------------")
    for i in range(len(matrix)):
        print(matrix[i])
    print("---------------")


n = int(input())
H = 0
PathLenght = 0
Str = []
Stb = []
res = []
result = []
StartMatrix = []
mtx = []
lll = []
coords = []

for i in range(n):
    # a = f'{random.randint(0, 100)} {random.randint(0, 100)}'
    list_point = list(map(int, input().split(' ')))
    mtx.append(list_point)
mtx.insert(0, [0, 0])
# mtx.append([1, 1])

# ctys = ['Boston', 'Phoenix', 'New York']
df = pd.DataFrame(mtx)
m = pd.DataFrame(distance_matrix(df.values, df.values))

print(m)
print()
print(mtx)

fig, ax = plt.subplots()

town = 1

for x, y in mtx:
    if x == 0 and y == 0:
        ax.add_patch(plt.Circle((x, y), 0.3, facecolor='#FF0000', alpha=1))
        plt.text(x - 0.12, y - 0.12, f'0')
    else:
        ax.add_patch(plt.Circle((x, y), 0.3, facecolor='#9ebcda', alpha=1))
        plt.text(x - 0.12, y - 0.12, f'{town}')
    town += 1

print()
matrix = m.values.tolist()
for i in range(len(matrix)):
    matrix[i][i] = float('inf')
    for g in range(len(matrix[i])):
        matrix[i][g] = round(matrix[i][g], 3)
print(matrix)
print('\n'.join([' '.join([str(cell) for cell in row]) for row in matrix]))
# Инициализируем массивы для сохранения индексов
for i in range(len(matrix)):
    Str.append(i)
    Stb.append(i)

# Сохраняем изначальную матрицу
for i in range(len(matrix)):
    StartMatrix.append(matrix[i].copy())


while True:
    # Редуцируем
    # --------------------------------------
    # Вычитаем минимальный элемент в строках
    for i in range(len(matrix)):
        min_row = min(matrix[i])
        min_column = min(row[i] for row in matrix)
        H += min_row + min_column
        for j in range(len(matrix)):
            matrix[i][j] -= min_row
            matrix[j][i] -= min_column
    # --------------------------------------
    # Оцениваем нулевые клетки и ищем нулевую клетку с максимальной оценкой
    # --------------------------------------
    NullMax = 0
    index1 = 0
    index2 = 0
    tmp = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                tmp = Min(matrix[i], j) + Min((row[j] for row in matrix), i)
                if tmp >= NullMax:
                    NullMax = tmp
                    index1 = i
                    index2 = j
                    lll.append((index1, index2))
    # --------------------------------------

    # Находим нужный нам путь, записываем его в res и удаляем все ненужное
    res.append(Str[index1] + 1)
    res.append(Stb[index2] + 1)

    oldIndex1 = Str[index1]
    oldIndex2 = Stb[index2]
    if oldIndex2 in Str and oldIndex1 in Stb:
        NewIndex1 = Str.index(oldIndex2)
        NewIndex2 = Stb.index(oldIndex1)
        matrix[NewIndex1][NewIndex2] = float('inf')
    del Str[index1]
    del Stb[index2]
    matrix = Delete(matrix, index1, index2)
    if len(matrix) == 1: break

# Формируем порядок пути
for i in range(0, len(res) - 1, 2):
    if res.count(res[i]) < 2:
        result.append(res[i])
        result.append(res[i + 1])
for i in range(0, len(res) - 1, 2):
    for j in range(0, len(res) - 1, 2):
        if result[len(result) - 1] == res[j]:
            result.append(res[j])
            result.append(res[j + 1])
print("----------------------------------")
result_sort = list(dict.fromkeys(result))
result_sort.reverse()

print(result)
print()

if len(result_sort) == n + 1:

    print(result_sort)
    print()

    for i in result_sort:
        coords.append(mtx[i - 1])

    # coords.insert(0, coords.pop())
    # coords.reverse()


    # Считаем длину пути
    for i in range(0, len(result) - 1, 2):
        if i == len(result) - 2:
            PathLenght += StartMatrix[result[i] - 1][result[i + 1] - 1]
            PathLenght += StartMatrix[result[i + 1] - 1][result[0] - 1]
        else:
            PathLenght += StartMatrix[result[i] - 1][result[i + 1] - 1]
    print(PathLenght)
    print("----------------------------------")

# else:
#     distance_matrix = np.array(StartMatrix)
#     result, distance = solve_tsp_dynamic_programming(distance_matrix)
#     print(result, distance)
#
#     for i in result:
#         coords.append(mtx[i - 1])

print(coords)
for i in range(len(coords)):
    if len(coords) > i + 1:
        plt.plot((coords[i][0], coords[i + 1][0]), (coords[i][1], coords[i + 1][1]), alpha=0.6)
    else:
        plt.plot((coords[-1][0], coords[0][0]), (coords[-1][1], coords[0][1]), alpha=0.6)
# Use adjustable='box-forced' to make the plot area square-shaped as well.
ax.set_aspect('equal', adjustable='datalim')
ax.set_xbound(3, 4)

ax.plot()  # Causes an autoscale update.
plt.show()