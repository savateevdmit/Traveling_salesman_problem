import random

import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from distance_calculation import get_list_distance

'''
50
145 78
170 168
176 74
98 141
186 27
120 169
37 110
198 13
169 77
56 140
180 14
170 78
73 110
64 61
131 147
37 157
5 157
2 0
155 59
124 136
28 13
35 56
59 143
126 71
117 89
65 43
100 183
189 70
30 45
21 69
24 191
187 160
14 171
91 64
91 170
80 9
46 150
110 181
9 0
167 78
109 170
175 70
18 28
89 160
121 8
127 176
51 175
142 185
195 117
152 48
'''

n = int(input())
coords2 = []
last_coords = []
last_coords2 = []
vip = []
mtx = []
population = []
st = []
dead_individuals = []
dict_populations = {}
way = []
stop = [0]

PERCENTAGE_OF_MUTATIONS = 80
NUMBER_OF_GENERATIONS = 50000
POPULATIONS = n * 3
CHILDREN = 2

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
    for i in range(len(vip)):
        st.append(i)

    for i in st:
        way.append(vip[i])
    dict_populations[str(st)] = sum(get_list_distance(way)[:-1])
    population.insert(0, st)

    for i in range(POPULATIONS):  # количество генераций начальных популяций
        way.clear()
        a = np.random.permutation(len(vip))
        popul = a.tolist()
        popul.insert(0, popul.pop(popul.index(0)))
        for i in popul:
            way.append(vip[i])
        dict_populations[str(popul)] = sum(get_list_distance(way)[:-1])
        if popul not in population:
            population.append(popul)
        else:
            a = np.random.permutation(n + 1)
            popul = a.tolist()
            popul.insert(0, popul.pop(popul.index(0)))
            population.append(popul)

    # print(dict_populations)
    # print()
    # print(population)
    # print()

    for i in range(NUMBER_OF_GENERATIONS):
        if len(dict_populations) < POPULATIONS:
            for i in range(POPULATIONS - len(dict_populations)):
                a = np.random.permutation(len(vip))
                popul = a.tolist()
                popul.insert(0, popul.pop(popul.index(0)))

                if str(popul) in dict_populations or str(popul) in dead_individuals:
                    a = np.random.permutation(len(vip))
                    popul = a.tolist()
                    popul.insert(0, popul.pop(popul.index(0)))

                way.clear()
                for i in popul:
                    way.append(vip[i])
                dict_populations[str(popul)] = sum(get_list_distance(way)[:-1])

        dct = list(dict_populations.keys())
        population = []
        for i in dct:
            population.append([int(x) for x in i[1:-1].split(', ')])

        # турнир родителей
        # -------------------
        # 1 тур
        q1 = random.choice(population)  # первый участник
        q2 = random.choice(population)

        # поиск победителя первого тура
        if dict_populations[str(q1)] > dict_populations[str(q2)]:
            win1 = q2
        else:
            win1 = q1

        # 2 тур
        qq1 = random.choice(population)  # первый участник
        qq2 = random.choice(population)  # второй участник

        # поиск победителя второго тура
        if dict_populations[str(qq1)] > dict_populations[str(qq2)]:
            win2 = qq2
        else:
            win2 = qq1

        parent1 = win1  # первый родитель
        parent2 = win2  # второй родитель

        point = random.randint(0, n - 1)  # генерация точки разрыва

        child1 = []  # первый ребёнок
        child2 = []  # второй ребёнок

        # -------
        # Первый ребенок
        if CHILDREN == 2:

            p1 = random.randint(0, n - 1)  # генерация первой точки разрыва
            p2 = random.randint(0, n - 1)  # генерация второй точки разрыва
            if p1 == p2:
                p2 = random.randint(0, n - 1)

            point1 = min(p1, p2)
            point2 = max(p1, p2)

            otr = parent1[point1:point2 + 1]

            for gen in range(len(parent2)):
                if parent2[gen] not in otr:
                    child1.extend([parent2[gen]])
                if gen == point1:
                    child1.extend(otr)

            # Второй ребёнок

            p1 = random.randint(0, n - 1)  # генерация первой точки разрыва
            p2 = random.randint(0, n - 1)  # генерация второй точки разрыва
            if p1 == p2:
                p2 = random.randint(0, n - 1)

            point1 = min(p1, p2)
            point2 = max(p1, p2)

            otr = parent2[point1:point2 + 1]

            for gen in range(len(parent1)):
                if parent1[gen] not in otr:
                    child2.extend([parent1[gen]])
                if gen == point1:
                    child2.extend(otr)

        elif CHILDREN == 1:
            point = random.randint(0, n - 1)  # генерация точки разрыва
            # print(point)
            # print()

            # формирование первого потомка
            child1 = parent1[:point + 1]
            for i in parent2[:]:
                if i not in child1:
                    child1.append(i)

            # print(child1)

            # формирование второго потомка
            child2 = parent2[:point + 1]
            for i in parent1[:]:
                if i not in child2:
                    child2.append(i)

        #  мутация

        mutation = random.randint(0, 100)
        # print(mutation)
        if mutation < PERCENTAGE_OF_MUTATIONS:
            # мутация первого потомка
            number1 = random.randint(1, len(vip) - 1)
            number2 = random.randint(1, len(vip) - 1)

            child1[number1], child1[number2] = child1[number2], child1[number1]

            # мутация второго потомка
            number1 = random.randint(1, len(vip) - 1)
            number2 = random.randint(1, len(vip) - 1)

            child2[number1], child2[number2] = child2[number2], child2[number1]

        # добавление потомков в общий словарь и удаление наименее приспособленных особей
        way.clear()
        for i in child1:
            way.append(vip[i])
        dict_populations[str(child1)] = sum(get_list_distance(way))

        way.clear()
        for i in child2:
            way.append(vip[i])
        dict_populations[str(child2)] = sum(get_list_distance(way))

        # удаление наименее приспособленных особей
        dict_populations = dict(sorted(dict_populations.items(), key=lambda item: item[1]))

        if list(dict_populations.values())[0] != stop[-1]:
            stop.clear()
            stop.append(list(dict_populations.values())[0])
        else:
            stop.append(list(dict_populations.values())[0])

        if len(stop) == 10000:
            break

        dead_individuals.append(list(dict_populations)[-1])
        dict_populations.pop(list(dict_populations)[-1])

        dead_individuals.append(list(dict_populations)[-1])
        dict_populations.pop(list(dict_populations)[-1])

        # print(dead_individuals)
        # print()
        # print(dict_populations)
        # print()

    # print('-------------------')
    dict_populations = dict(sorted(dict_populations.items(), key=lambda item: item[1]))

    dct = list(dict_populations.keys())
    population.clear()

    for i in dct:
        population = [int(x) for x in i[1:-1].split(', ')]
        break
    # print(population, dict_populations[next(iter(dict_populations))])

    for i in population:
        last_coords.append(vip[i])

    # print(last_coords)
    last = last_coords[-1]
    # del last_coords[-1]
    mtx.insert(0, last)
    mtx.append([0, 0])
    st.clear()
    dict_populations.clear()

    for i in range(len(mtx)):
        st.append(i)

    for i in st:
        way.append(mtx[i])
    dict_populations[str(st)] = sum(get_list_distance(way)[:-1])
    population.insert(0, st)

    for i in range(POPULATIONS):  # количество генераций начальных популяций
        way.clear()
        a = np.random.permutation(len(mtx))
        popul = a.tolist()
        popul.insert(0, popul.pop(popul.index(0)))
        popul.insert(len(mtx) - 1, popul.pop(popul.index(len(mtx) - 1)))
        for i in popul:
            way.append(mtx[i])
        dict_populations[str(popul)] = sum(get_list_distance(way)[:-1])
        if popul not in population:
            population.append(popul)
        else:
            a = np.random.permutation(n + 1)
            popul = a.tolist()
            popul.insert(0, popul.pop(popul.index(0)))
            popul.insert(len(mtx) - 1, popul.pop(popul.index(len(mtx) - 1)))
            population.append(popul)

    # print(dict_populations)
    # print()
    # print(population)
    # print()

    for i in range(NUMBER_OF_GENERATIONS):
        if len(dict_populations) < POPULATIONS:
            for i in range(POPULATIONS - len(dict_populations)):
                a = np.random.permutation(len(mtx))
                popul = a.tolist()
                popul.insert(0, popul.pop(popul.index(0)))
                popul.insert(len(mtx) - 1, popul.pop(popul.index(len(mtx) - 1)))

                if str(popul) in dict_populations or str(popul) in dead_individuals:
                    a = np.random.permutation(len(mtx))
                    popul = a.tolist()
                    popul.insert(0, popul.pop(popul.index(0)))
                    popul.insert(len(mtx) - 1, popul.pop(popul.index(len(mtx) - 1)))

                way.clear()
                for i in popul:
                    way.append(mtx[i])
                dict_populations[str(popul)] = sum(get_list_distance(way)[:-1])

        dct = list(dict_populations.keys())
        population = []
        for i in dct:
            population.append([int(x) for x in i[1:-1].split(', ')])

        # турнир родителей
        # -------------------

        # 1 тур
        q1 = random.choice(population)  # первый участник
        q2 = random.choice(population)
        # второй участник

        # print(q1, q2)
        # print(dict_populations[str(q1)], dict_populations[str(q2)])

        if dict_populations[str(q1)] > dict_populations[str(q2)]:  # поиск победителя первого тура
            win1 = q2
        else:
            win1 = q1

        # 2 тур
        qq1 = random.choice(population)  # первый участник
        qq2 = random.choice(population)  # второй участник

        if dict_populations[str(qq1)] > dict_populations[str(qq2)]:  # поиск победителя второго тура
            win2 = qq2
        else:
            win2 = qq1

        parent1 = win1  # первый родитель
        parent2 = win2  # второй родитель
        child1 = []  # первый ребёнок
        child2 = []  # второй ребёнок

        # -------
        # Первый ребенок
        if CHILDREN == 2:

            p1 = random.randint(0, n - 1)  # генерация первой точки разрыва
            p2 = random.randint(0, n - 1)  # генерация второй точки разрыва
            if p1 == p2:
                p2 = random.randint(0, n - 1)

            point1 = min(p1, p2)
            point2 = max(p1, p2)

            otr = parent1[point1:point2 + 1]

            for gen in range(len(parent2)):
                if parent2[gen] not in otr:
                    child1.extend([parent2[gen]])
                if gen == point1:
                    child1.extend(otr)

            # Второй ребёнок

            p1 = random.randint(0, n - 1)  # генерация первой точки разрыва
            p2 = random.randint(0, n - 1)  # генерация второй точки разрыва
            if p1 == p2:
                p2 = random.randint(0, n - 1)

            point1 = min(p1, p2)
            point2 = max(p1, p2)

            otr = parent2[point1:point2 + 1]

            for gen in range(len(parent1)):
                if parent1[gen] not in otr:
                    child2.extend([parent1[gen]])
                if gen == point1:
                    child2.extend(otr)

        elif CHILDREN == 1:
            point = random.randint(0, n - 1)  # генерация точки разрыва
            # print(point)
            # print()

            # формирование первого потомка
            child1 = parent1[:point + 1]
            for i in parent2[:]:
                if i not in child1:
                    child1.append(i)

            # print(child1)

            # формирование второго потомка
            child2 = parent2[:point + 1]
            for i in parent1[:]:
                if i not in child2:
                    child2.append(i)

        #  мутация

        mutation = random.randint(0, 100)
        # print(mutation)
        if mutation < PERCENTAGE_OF_MUTATIONS:
            # мутация первого потомка
            number1 = random.randint(1, len(mtx) - 1)
            number2 = random.randint(1, len(mtx) - 1)

            child1[number1], child1[number2] = child1[number2], child1[number1]

            # мутация второго потомка
            number1 = random.randint(1, len(mtx) - 1)
            number2 = random.randint(1, len(mtx) - 1)

            child2[number1], child2[number2] = child2[number2], child2[number1]

        # добавление потомков в общий словарь и удаление наименее приспособленных особей
        way.clear()
        for i in child1:
            way.append(mtx[i])
        dict_populations[str(child1)] = sum(get_list_distance(way)[:-1])

        way.clear()
        for i in child2:
            way.append(mtx[i])
        dict_populations[str(child2)] = sum(get_list_distance(way)[:-1])

        # удаление наименее приспособленных особей
        dict_populations = dict(sorted(dict_populations.items(), key=lambda item: item[1]))

        if list(dict_populations.values())[0] != stop[-1]:
            stop.clear()
            stop.append(list(dict_populations.values())[0])
        else:
            stop.append(list(dict_populations.values())[0])

        if len(stop) == 10000:
            break

        dead_individuals.append(list(dict_populations)[-1])
        dict_populations.pop(list(dict_populations)[-1])

        dead_individuals.append(list(dict_populations)[-1])
        dict_populations.pop(list(dict_populations)[-1])

        # print(dead_individuals)
        # print()
        # print(dict_populations)
        # print()

    # print('-------------------')
    dict_populations = dict(sorted(dict_populations.items(), key=lambda item: item[1]))

    dct = list(dict_populations.keys())
    population.clear()

    for i in dct:
        population = [int(x) for x in i[1:-1].split(', ')]
        break
    # print(population, dict_populations[next(iter(dict_populations))])

    for i in population:
        last_coords2.append(mtx[i])

    # print(last_coords2)

else:
    for i in range(n + 1):
        st.append(i)

    for i in st:
        way.append(mtx[i])
    dict_populations[str(st)] = sum(get_list_distance(way))
    population.insert(0, st)

    for i in range(POPULATIONS):  # количество генераций начальных популяций
        way.clear()
        a = np.random.permutation(n + 1)
        popul = a.tolist()
        popul.insert(0, popul.pop(popul.index(0)))
        for i in popul:
            way.append(mtx[i])
        dict_populations[str(popul)] = sum(get_list_distance(way))
        if popul not in population:
            population.append(popul)
        else:
            a = np.random.permutation(n + 1)
            popul = a.tolist()
            popul.insert(0, popul.pop(popul.index(0)))
            population.append(popul)

    # print(dict_populations)
    # print()
    # print(population)
    # print()

    # for i in tqdm(range(NUMBER_OF_GENERATIONS), position=0, leave=True):
    for ii in range(NUMBER_OF_GENERATIONS):
        if len(dict_populations) < POPULATIONS:
            for i in range(POPULATIONS - len(dict_populations)):
                a = np.random.permutation(n + 1)
                popul = a.tolist()
                popul.insert(0, popul.pop(popul.index(0)))

                while str(popul) in dict_populations or str(popul) in dead_individuals:
                    a = np.random.permutation(n + 1)
                    popul = a.tolist()
                    popul.insert(0, popul.pop(popul.index(0)))

                way.clear()
                for i in popul:
                    way.append(mtx[i])
                dict_populations[str(popul)] = sum(get_list_distance(way))

        dct = list(dict_populations.keys())
        population = []
        for i in dct:
            population.append([int(x) for x in i[1:-1].split(', ')])

        # турнир родителей
        # -------------------

        # 1 тур
        q1 = random.choice(population)  # первый участник
        q2 = random.choice(population)  # второй участник

        if dict_populations[str(q1)] > dict_populations[str(q2)]:  # поиск победителя первого тура
            win1 = q2
            # dead_individuals.append(list(dict_populations)[-1])
        else:
            win1 = q1

        # 2 тур
        qq1 = random.choice(population)  # первый участник
        qq2 = random.choice(population)  # второй участник

        if dict_populations[str(qq1)] > dict_populations[str(qq2)]:  # поиск победителя второго тура
            win2 = qq2
        else:
            win2 = qq1

        parent1 = win1  # первый родитель
        parent2 = win2  # второй родитель

        child1 = []  # первый ребёнок
        child2 = []  # второй ребёнок

        # -------
        # Первый ребенок
        if CHILDREN == 2:

            p1 = random.randint(0, n - 1)  # генерация первой точки разрыва
            p2 = random.randint(0, n - 1)  # генерация второй точки разрыва
            if p1 == p2:
                p2 = random.randint(0, n - 1)

            point1 = min(p1, p2)
            point2 = max(p1, p2)

            otr = parent1[point1:point2 + 1]

            for gen in range(len(parent2)):
                if parent2[gen] not in otr:
                    child1.extend([parent2[gen]])
                if gen == point1:
                    child1.extend(otr)

            # Второй ребёнок

            p1 = random.randint(0, n - 1)  # генерация первой точки разрыва
            p2 = random.randint(0, n - 1)  # генерация второй точки разрыва
            if p1 == p2:
                p2 = random.randint(0, n - 1)

            point1 = min(p1, p2)
            point2 = max(p1, p2)

            otr = parent2[point1:point2 + 1]

            for gen in range(len(parent1)):
                if parent1[gen] not in otr:
                    child2.extend([parent1[gen]])
                if gen == point1:
                    child2.extend(otr)

        elif CHILDREN == 1:
            point = random.randint(0, n - 1)  # генерация точки разрыва
            # print(point)
            # print()

            # формирование первого потомка
            child1 = parent1[:point + 1]
            for i in parent2[:]:
                if i not in child1:
                    child1.append(i)

            # print(child1)

            # формирование второго потомка
            child2 = parent2[:point + 1]
            for i in parent1[:]:
                if i not in child2:
                    child2.append(i)

        # parent1 = [0, 6, 2, 7, 3, 8, 1, 4, 9, 5]
        # parent2 = [0, 3, 9, 4, 1, 7, 5, 6, 2, 8]

        # point = random.randint(0, n - 1)  # генерация точки разрыва
        # # print(point)
        # # print()
        #
        # # формирование первого потомка
        # child1 = parent1[:point + 1]
        # for i in parent2[:]:
        #     if i not in child1:
        #         child1.append(i)
        #
        # # print(child1)
        #
        # # формирование второго потомка
        # child2 = parent2[:point + 1]
        # for i in parent1[:]:
        #     if i not in child2:
        #         child2.append(i)
        #
        # # print(child2)
        # # print()

        #  мутация

        mutation = random.randint(0, 100)
        # print(mutation)
        if mutation < PERCENTAGE_OF_MUTATIONS:
            # мутация первого потомка
            number1 = random.randint(1, n - 1)
            number2 = random.randint(1, n - 1)

            child1[number1], child1[number2] = child1[number2], child1[number1]

            # мутация второго потомка
            number1 = random.randint(1, n - 1)
            number2 = random.randint(1, n - 1)

            child2[number1], child2[number2] = child2[number2], child2[number1]


        # добавление потомков в общий словарь и удаление наименее приспособленных особей
        way.clear()
        for i in child1:
            way.append(mtx[i])
        dict_populations[str(child1)] = sum(get_list_distance(way))

        way.clear()
        for i in child2:
            way.append(mtx[i])
        dict_populations[str(child2)] = sum(get_list_distance(way))

        # удаление наименее приспособленных особей
        dict_populations = dict(sorted(dict_populations.items(), key=lambda item: item[1]))

        if list(dict_populations.values())[0] != stop[-1]:
            stop.clear()
            stop.append(list(dict_populations.values())[0])
        else:
            stop.append(list(dict_populations.values())[0])

        if len(stop) == 10000:
            break

        print(list(dict_populations.values())[0], ii)
        dead_individuals.append(list(dict_populations)[-1])
        dict_populations.pop(list(dict_populations)[-1])

        dead_individuals.append(list(dict_populations)[-1])
        dict_populations.pop(list(dict_populations)[-1])

        # print(dead_individuals)
        # print()
        # print(dict_populations)
        # print()

    # print('-------------------')
    dict_populations = dict(sorted(dict_populations.items(), key=lambda item: item[1]))

    dct = list(dict_populations.keys())
    population.clear()

    for i in dct:
        population = [int(x) for x in i[1:-1].split(', ')]
        break
    # print(population, dict_populations[next(iter(dict_populations))])

    for i in population:
        last_coords.append(mtx[i])

    # print(last_coords)

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
    # print(last_coords2)

    for i in range(len(last_coords2)):
        if len(last_coords2) > i + 1:
            plt.plot((last_coords2[i][0], last_coords2[i + 1][0]), (last_coords2[i][1], last_coords2[i + 1][1]), alpha=0.2)
        # else:
        #     plt.plot((last_coords2[-1][0], last_coords2[0][0]), (last_coords2[-1][1], last_coords2[0][1]), alpha=0.6)

last_coords3 = []

for i in last_coords:
    if i not in last_coords3:
        last_coords3.append(i)

for i in last_coords2:
    if i not in last_coords3:
        last_coords3.append(i)

print(last_coords3, sum(get_list_distance(last_coords3)))

# Use adjustable='box-forced' to make the plot area square-shaped as well.
ax.set_aspect('equal', adjustable='datalim')
ax.set_xbound(3, 4)

ax.plot()  # Causes an autoscale update.
plt.show()
