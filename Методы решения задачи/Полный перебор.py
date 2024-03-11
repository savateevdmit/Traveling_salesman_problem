# с возвратом в начальные координаты

import time
import itertools
from copy import copy

import matplotlib.pyplot as plt
from distance_calculation import get_list_distance

fig, ax = plt.subplots()

route = 0
list_points = []
town = 1
coords = []
dict_coords = {}
number_towns_list = []
shortest_path = 100000
mtx = []
vip = []

for i in range(int(input())):
    # a = f'{random.randint(0, 100)} {random.randint(0, 100)}'
    list_point = list(map(int, input().split(' ')))
    coords.append(list_point[:2])
    if len(list_point) == 3:
        vip.append(list_point[:2])
    else:
        mtx.append(list_point)

if len(vip) != 0:
    vip.insert(0, [0, 0])
coords.insert(0, (0, 0))

t1 = time.time()
for i in coords:
    if i not in vip:
        dict_coords[town] = (i[0], i[1])
        number_towns_list.append(town)
        if i[0] == 0 and i[1] == 0:
            ax.add_patch(plt.Circle((i[0], i[1]), 0.3, facecolor='#FF0000', alpha=1))
        else:
            ax.add_patch(plt.Circle((i[0], i[1]), 0.3, facecolor='#9ebcda', alpha=1))

        plt.text(i[0] - 0.12, i[1] - 0.12, f'{town}')
        town += 1
    else:
        dict_coords[town] = (i[0], i[1])
        number_towns_list.append(town)
        if i[0] == 0 and i[1] == 0:
            ax.add_patch(plt.Circle((i[0], i[1]), 0.4, facecolor='#FF0000', alpha=1))
        else:
            ax.add_patch(plt.Circle((i[0], i[1]), 0.4, facecolor='#FF8C00', alpha=1))

        plt.text(i[0] - 0.12, i[1] - 0.12, f'{town}')
        town += 1

for i in itertools.permutations(number_towns_list):
    for j in i:
        if list(dict_coords[int(j)]) not in vip:
            list_points.append(dict_coords[int(j)])
    if len(vip) > 0:
        for i in vip:
            list_points.insert(0, (i[0], i[1]))
    else:
        list_points.insert(0, (0, 0))

    print(list_points)
    distance = sum(get_list_distance(list_points))
    print(get_list_distance(list_points)[:-1])
    if distance < shortest_path:
        shortest_path = distance
        route = copy(list_points)
    list_points.clear()

b = route[route[1:].index((0, 0)) + 1:]

del route[route[1:].index((0, 0)) + 1:]
route.reverse()
b.reverse()
for i in b:
    route.append(i)

route.insert(0, route.pop())

t2 = time.time()
print(f'Самый короткий путь: {shortest_path}, маршрут: {route}')
print(f'Потраченное время: {t2 - t1}')

for i in range(len(route)):
    if len(route) > i + 1:
        plt.plot((route[i][0], route[i + 1][0]), (route[i][1], route[i + 1][1]), alpha=0.6)
    else:
        plt.plot((route[-1][0], route[0][0]), (route[-1][1], route[0][1]), alpha=0.6)

# Use adjustable='box-forced' to make the plot area square-shaped as well.
ax.set_aspect('equal', adjustable='datalim')
ax.set_xbound(3, 4)

ax.plot()  # Causes an autoscale update.
plt.show()

'''
5
4 9
6 2
5 7
6 1
6 9

7
1 0
1 1
1 2
1 3
1 4
1 5
1 6

7
4 9
6 2
5 7
6 1
0 0
7 3
1 0

6
4 9
6 2 1
5 7
6 1
7 3 1
1 0

7
3787 4712 1
3280 1554
529 3505 1
2732 430 1
3761 3517 1
2892 2501
1253 4976

8
2250 1041 1
1692 3551 1
2791 2254
3018 3051 1
2464 1366
4040 830
3719 2683 1
2058 1087
'''