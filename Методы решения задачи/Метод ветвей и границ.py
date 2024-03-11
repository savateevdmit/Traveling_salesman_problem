import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from distance_calculation import get_list_distance
from python_tsp.heuristics import solve_tsp_local_search
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
coords2 = []
vip = []
first = []
last_coords = []


for i in range(n):
    # a = f'{random.randint(0, 100)} {random.randint(0, 100)}'
    list_point = list(map(int, input().split(' ')))
    if len(list_point) == 3:
        vip.append(list_point[:2])
    else:
        mtx.append(list_point)

if len(vip) != 0:
    vip.insert(0, [0, 0])
# else:

df_vip = pd.DataFrame(vip)
m_vip = pd.DataFrame(distance_matrix(df_vip.values, df_vip.values))

# print(m)
# print()
# print(mtx)

fig, ax = plt.subplots()

town = 1

for x, y in vip:
    if x == 0 and y == 0:
        ax.add_patch(plt.Circle((x, y), (0.95 / (n + (n / 0.75))) * n, facecolor='#FF0000', alpha=1))
        # plt.text(x - 0.12, y - 0.12, f'0')
    else:
        ax.add_patch(plt.Circle((x, y), (0.95 / (n + (n / 0.75))) * n, facecolor='#FF8C00', alpha=1))
        # plt.text(x - 0.12, y - 0.12, f'{town}')
    town += 1

print()
matrix_vip = m_vip.values.tolist()

if len(matrix_vip) > 0:
    for i in range(len(matrix_vip)):
        matrix_vip[i][i] = float('inf')
        for g in range(len(matrix_vip[i])):
            matrix_vip[i][g] = round(matrix_vip[i][g], 3)
    print(matrix_vip)
    print('\n'.join([' '.join([str(cell) for cell in row]) for row in matrix_vip]))
    # Инициализируем массивы для сохранения индексов
    for i in range(len(matrix_vip)):
        Str.append(i)
        Stb.append(i)

    # Сохраняем изначальную матрицу
    for i in range(len(matrix_vip)):
        StartMatrix.append(matrix_vip[i].copy())

    while True:
        # Редуцируем
        # --------------------------------------
        # Вычитаем минимальный элемент в строках
        for i in range(len(matrix_vip)):
            min_row = min(matrix_vip[i])
            min_column = min(row[i] for row in matrix_vip)
            H += min_row + min_column
            for j in range(len(matrix_vip)):
                matrix_vip[i][j] -= min_row
                matrix_vip[j][i] -= min_column
        # --------------------------------------
        # Оцениваем нулевые клетки и ищем нулевую клетку с максимальной оценкой
        # --------------------------------------
        NullMax = 0
        index1 = 0
        index2 = 0
        tmp = 0
        for i in range(len(matrix_vip)):
            for j in range(len(matrix_vip)):
                if matrix_vip[i][j] == 0:
                    tmp = Min(matrix_vip[i], j) + Min((row[j] for row in matrix_vip), i)
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
            matrix_vip[NewIndex1][NewIndex2] = float('inf')
        del Str[index1]
        del Stb[index2]
        matrix_vip = Delete(matrix_vip, index1, index2)
        if len(matrix_vip) == 1: break

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

    # print(result)
    print(result_sort)
    print()

    if len(result_sort) == len(vip):

        # print(result_sort)
        # print()

        for i in result_sort:
            coords2.append(vip[i - 1])
            if vip[i - 1] != [0, 0]:
                last_coords.append(vip[i - 1])
            else:
                last_coords.insert(0, vip[i - 1])
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
        print(coords2)
        print("----------------------------------")

    else:
        dm = np.array(StartMatrix)
        result, distance = solve_tsp_local_search(dm)
        print(result, distance)

        for i in result:
            coords2.append(vip[i])
            if vip[i] != [0, 0]:
                last_coords.append(vip[i])
            else:
                last_coords.insert(0, vip[i])

    if [0, 0] in coords2:
        coords2.remove([0, 0])
        coords2.insert(0, [0, 0])

    print(coords2)
    first.append(coords2[-1])
    for i in range(len(coords2)):
        if len(coords2) > i + 1:
            plt.plot((coords2[i][0], coords2[i + 1][0]), (coords2[i][1], coords2[i + 1][1]), alpha=0.6)
        # else:
        #     plt.plot((coords[-1][0], coords[0][0]), (coords[-1][1], coords[0][1]), alpha=0.6)


StartMatrix.clear()
coords2.clear()

mtx.insert(0, [0, 0])

if len(first) > 0:
    mtx.insert(0, first[0])

# mtx.append([1, 1])

# ctys = ['Boston', 'Phoenix', 'New York']
df = pd.DataFrame(mtx)
m = pd.DataFrame(distance_matrix(df.values, df.values))

town = 1

for i in mtx:
    if i not in vip:
        if i[0] == 0 and i[1] == 0:
            ax.add_patch(plt.Circle((i[0], i[1]), (0.75 / (n + (n / 0.55))) * n, facecolor='#FF0000', alpha=1))
            # plt.text(x - 0.12, y - 0.12, f'0')
        else:
            ax.add_patch(plt.Circle((i[0], i[1]), (0.75 / (n + (n / 0.55))) * n, facecolor='#9ebcda', alpha=1))
            # plt.text(x - 0.12, y - 0.12, f'{town}')
        town += 1

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
        # Str = list(dict.fromkeys(Str))
        # Stb = list(dict.fromkeys(Stb))

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
print(result_sort)
print()

if len(result_sort) == len(mtx):

    print(result_sort)
    print()

    for i in result_sort:
        coords2.append(mtx[i - 1])
        last_coords.append(mtx[i - 1])
        # else:
        #     last_coords.insert(0, mtx[i - 1])

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

else:
    dm = np.array(StartMatrix)
    result, distance = solve_tsp_local_search(dm)
    print(result, distance)

    for i in result:
        coords2.append(mtx[i])
        last_coords.append(mtx[i])
        # else:
        #     last_coords.insert(0, mtx[i])

print('*******************************')
# last_coords[-2], last_coords[-1] = last_coords[-1], last_coords[-2]
# last_coords[-3], last_coords[-2:] = last_coords[-2:], last_coords[-3]

last_coords2 = []

if last_coords.count([0, 0]) > 1:
    b = last_coords[last_coords[1:].index([0, 0]) + 1:]

    del last_coords[last_coords[1:].index([0, 0]) + 1:]
    b.reverse()
    for i in b:
        last_coords.append(i)
# print(last_coords)

for i in last_coords:
    if i not in last_coords2:
        last_coords2.append(i)

print(last_coords2)
print(sum(get_list_distance(last_coords2)))

for i in range(len(coords2)):
    if len(coords2) > i + 1 and coords2[i + 1] == [0, 0]:
        plt.plot((coords2[i][0], coords2[-1][0]), (coords2[i][1], coords2[-1][1]), alpha=0.2)

    elif len(coords2) > i + 1:
        plt.plot((coords2[i][0], coords2[i + 1][0]), (coords2[i][1], coords2[i + 1][1]), alpha=0.6)

    elif len(vip) == 0:
        plt.plot((coords2[-1][0], coords2[0][0]), (coords2[-1][1], coords2[0][1]), alpha=0.6)

ax.set_aspect('equal', adjustable='datalim')
ax.set_xbound(3, 4)

ax.plot()  # Causes an autoscale update.
plt.show()

