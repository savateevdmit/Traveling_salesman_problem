import numpy as np
from matplotlib import pyplot as plt

from distance_calculation import get_list_distance


n = int(input())
coords2 = []
last_coords = []
last_coords2 = []
last = []
vip = []
mtx = []
population = []
dict_populations = {}
dict_populations2 = {}
way = []
POPULATIONS = n * 3

for i in range(n):
    # a = f'{random.randint(0, 100)} {random.randint(0, 100)}'
    list_point = list(map(int, input().split(' ')))
    coords2.append(list_point[:2])
    if len(list_point) == 3:
        vip.append(list_point[:2])
    else:
        mtx.append(list_point)

if len(vip) != 0:
    vip.insert(0, [0, 0])
else:
    mtx.insert(0, [0, 0])
coords2.insert(0, [0, 0])

if len(vip) > 0:
    for i in range(POPULATIONS * (len(vip))):  # количество генераций начальных популяций
        way.clear()
        a = np.random.permutation(len(vip))
        popul = a.tolist()
        popul.insert(0, popul.pop(popul.index(0)))
        for i in popul:
            way.append(vip[i])
        dict_populations[str(popul)] = sum(get_list_distance(way)[:-1])

    dict_populations = dict(sorted(dict_populations.items(), key=lambda item: item[1]))

    dct = list(dict_populations.keys())
    for i in dct:
        population = [int(x) for x in i[1:-1].split(', ')]
        break

    for i in population:
        last_coords.append(vip[i])


    last = last_coords[-1]
    # del last_coords[-1]
    mtx.insert(0, last)
    mtx.append([0, 0])

    for i in range(POPULATIONS * (n - len(vip) + 1)):  # количество генераций начальных популяций
        way.clear()
        a = np.random.permutation(len(mtx))
        popul = a.tolist()
        popul.insert(0, popul.pop(popul.index(0)))
        popul.insert(len(mtx) - 1, popul.pop(popul.index(len(mtx) - 1)))
        for i in popul:
            way.append(mtx[i])
        dict_populations2[str(popul)] = sum(get_list_distance(way)[:-1])

    dict_populations2 = dict(sorted(dict_populations2.items(), key=lambda item: item[1]))

    dct = list(dict_populations2.keys())
    for i in dct:
        population = [int(x) for x in i[1:-1].split(', ')]
        break

    for i in population:
        last_coords2.append(mtx[i])



else:
    for i in range(POPULATIONS * n):  # количество генераций начальных популяций
        way.clear()
        a = np.random.permutation(n + 1)
        popul = a.tolist()
        popul.insert(0, popul.pop(popul.index(0)))
        for i in popul:
            way.append(mtx[i])
        dict_populations[str(popul)] = sum(get_list_distance(way))

    dict_populations = dict(sorted(dict_populations.items(), key=lambda item: item[1]))

    dct = list(dict_populations.keys())
    for i in dct:
        population = [int(x) for x in i[1:-1].split(', ')]
        break

    for i in population:
        last_coords.append(mtx[i])


fig, ax = plt.subplots()

town = 1

if len(vip) == 0:
    for x, y in mtx:
        if x == 0 and y == 0:
            ax.add_patch(plt.Circle((x, y), (0.95 / (n + (n / 0.75))) * n, facecolor='#FF0000', alpha=1))
            # plt.text(x - 0.12, y - 0.12, f'0')
        else:
            ax.add_patch(plt.Circle((x, y), (0.95 / (n + (n / 0.75))) * n, facecolor='#9ebcda', alpha=1))
            # plt.text(x - 0.12, y - 0.12, f'{town}')
        town += 1

    for i in range(len(last_coords)):
        if len(last_coords) > i + 1:
            plt.plot((last_coords[i][0], last_coords[i + 1][0]), (last_coords[i][1], last_coords[i + 1][1]), alpha=0.6)
        else:
            plt.plot((last_coords[-1][0], last_coords[0][0]), (last_coords[-1][1], last_coords[0][1]), alpha=0.6)

else:
    for x, y in mtx:
        if x == 0 and y == 0:
            ax.add_patch(plt.Circle((x, y), (0.95 / (n + (n / 0.75))) * n, facecolor='#FF0000', alpha=1))
            # plt.text(x - 0.12, y - 0.12, f'0')
        else:
            ax.add_patch(plt.Circle((x, y), (0.95 / (n + (n / 0.75))) * n, facecolor='#9ebcda', alpha=1))
            # plt.text(x - 0.12, y - 0.12, f'{town}')
        town += 1

    for x, y in vip:
        if x == 0 and y == 0:
            ax.add_patch(plt.Circle((x, y), (0.95 / (n + (n / 0.75))) * n, facecolor='#FF0000', alpha=1))
            # plt.text(x - 0.12, y - 0.12, f'0')
        else:
            ax.add_patch(plt.Circle((x, y), (0.95 / (n + (n / 0.75))) * n, facecolor='#FF8C00', alpha=1))
            # plt.text(x - 0.12, y - 0.12, f'{town}')
        town += 1

    for i in range(len(last_coords)):
        if len(last_coords) > i + 1:
            plt.plot((last_coords[i][0], last_coords[i + 1][0]), (last_coords[i][1], last_coords[i + 1][1]), alpha=0.6)
    print(last_coords2)

    for i in range(len(last_coords2)):
        if len(last_coords2) > i + 1:
            plt.plot((last_coords2[i][0], last_coords2[i + 1][0]), (last_coords2[i][1], last_coords2[i + 1][1]), alpha=0.2)
        # else:
        #     plt.plot((last_coords2[-1][0], last_coords2[0][0]), (last_coords2[-1][1], last_coords2[0][1]), alpha=0.6)

# Use adjustable='box-forced' to make the plot area square-shaped as well.
ax.set_aspect('equal', adjustable='datalim')
ax.set_xbound(3, 4)

ax.plot()  # Causes an autoscale update.
plt.show()

last_coords3 = []

for i in last_coords:
    if i not in last_coords3:
        last_coords3.append(i)

for i in last_coords2:
    if i not in last_coords3:
        last_coords3.append(i)

print(last_coords3, sum(get_list_distance(last_coords3)))