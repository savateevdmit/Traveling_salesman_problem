from multiprocessing import Process
import random

import numpy as np

from distance_calculation import get_list_distance

def func1():
    NG = [150000]  # количество генераций
    PM = [10]  # процент мутаций
    PPL = [6]  # количество особей в популяции
    CHL = [1]  # количество точек разрыва

    k = 0
    for ng in NG:
        for pm in PM:
            for ppl in PPL:
                for chl in CHL:
                    n = 85
                    coords2 = []
                    vip = []
                    mtx = []
                    last_coords = []
                    last_coords2 = []
                    population = []
                    st = []
                    dead_individuals = []
                    dict_populations = {}
                    way = []
                    stop = [0]
                    PERCENTAGE_OF_MUTATIONS = pm
                    NUMBER_OF_GENERATIONS = ng
                    POPULATIONS = ppl * n
                    CHILDREN = chl
                    itog = []
                    a = [[182, 111], [77, 104], [182, 90], [182, 102], [116, 166], [174, 140], [145, 125], [86, 59], [83, 182], [131, 155], [140, 151], [144, 58], [12, 162], [112, 153], [172, 0], [39, 23], [39, 167], [118, 91], [14, 80], [12, 70], [164, 24], [16, 187], [140, 119], [50, 58], [189, 174], [110, 5], [114, 63], [115, 149], [94, 97], [161, 181], [129, 53], [126, 13], [200, 125], [81, 185], [151, 5], [6, 128], [12, 3], [10, 28], [155, 139], [64, 11], [127, 190], [8, 47], [124, 9], [124, 159], [172, 67], [131, 100], [80, 20], [109, 164], [53, 89], [17, 155], [176, 107], [199, 115], [93, 175], [101, 1], [70, 133], [83, 143], [188, 32], [53, 183], [154, 90], [47, 109], [9, 140], [155, 162], [5, 54], [127, 156], [155, 129], [52, 191], [177, 156], [26, 90], [69, 127], [185, 33], [101, 36], [108, 86], [80, 5], [94, 3], [115, 199], [113, 3], [145, 43], [174, 148], [17, 52], [61, 96], [122, 133], [40, 169], [31, 187], [181, 120], [19, 72]]
                    for i in a:
                        # b = random.choice([0, 0])
                        # a = f'{random.randint(0, 200)} {random.randint(0, 200)}'
                        # print(a)
                        # list_point = list(map(int, a.split(' ')))
                        coords2.append(i[:2])
                        if len(i) == 3:
                            vip.append(i[:2])
                        else:
                            mtx.append(i)

                    if len(vip) != 0:
                        vip.insert(0, [0, 0])
                    else:
                        mtx.insert(0, [0, 0])
                    coords2.insert(0, [0, 0])

                    for _ in range(10):
                        # print('----------')
                        last_coords = []
                        last_coords2 = []
                        population = []
                        st = []
                        dead_individuals = []
                        dict_populations = {}
                        way = []
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
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

                                    child1[number1], child1[number2] = child1[number2], child1[number1]

                                    # мутация второго потомка
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

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

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                if list(dict_populations.values())[0] != stop[-1]:
                                    stop.clear()
                                    stop.append(list(dict_populations.values())[0])
                                else:
                                    stop.append(list(dict_populations.values())[0])

                                if len(stop) == 10000:
                                    break

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

                                if dict_populations[str(q1)] > dict_populations[
                                    str(q2)]:  # поиск победителя первого тура
                                    win1 = q2
                                else:
                                    win1 = q1

                                # 2 тур
                                qq1 = random.choice(population)  # первый участник
                                qq2 = random.choice(population)  # второй участник

                                if dict_populations[str(qq1)] > dict_populations[
                                    str(qq2)]:  # поиск победителя второго тура
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
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

                                    child1[number1], child1[number2] = child1[number2], child1[number1]

                                    # мутация второго потомка
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

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

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                if list(dict_populations.values())[0] != stop[-1]:
                                    stop.clear()
                                    stop.append(list(dict_populations.values())[0])
                                else:
                                    stop.append(list(dict_populations.values())[0])

                                if len(stop) == 10000:
                                    break

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
                            for i in range(NUMBER_OF_GENERATIONS):
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

                                if dict_populations[str(q1)] > dict_populations[
                                    str(q2)]:  # поиск победителя первого тура
                                    win1 = q2
                                    # dead_individuals.append(list(dict_populations)[-1])
                                else:
                                    win1 = q1

                                # 2 тур
                                qq1 = random.choice(population)  # первый участник
                                qq2 = random.choice(population)  # второй участник

                                if dict_populations[str(qq1)] > dict_populations[
                                    str(qq2)]:  # поиск победителя второго тура
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
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

                                    child1[number1], child1[number2] = child1[number2], child1[number1]

                                    # мутация второго потомка
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

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

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                if list(dict_populations.values())[0] != stop[-1]:
                                    stop.clear()
                                    stop.append(list(dict_populations.values())[0])
                                else:
                                    stop.append(list(dict_populations.values())[0])

                                if len(stop) == 10000:
                                    break

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

                        last_coords3 = []
                        # print(last_coords3)

                        for i in last_coords:
                            if i not in last_coords3:
                                last_coords3.append(i)

                        for i in last_coords2:
                            if i not in last_coords3:
                                last_coords3.append(i)

                        # print(sum(get_list_distance(last_coords3)))
                        itog.append(sum(get_list_distance(last_coords3)))
                    print()
                    print(f"{itog} ({sum(itog) / 10}), ng = {ng}, pm = {pm}, ppl = {ppl}, chl = {chl}")


def func2():
    NG = [150000]  # количество генераций
    PM = [10]  # процент мутаций
    PPL = [6]  # количество особей в популяции
    CHL = [2]  # количество точек разрыва

    k = 0
    for ng in NG:
        for pm in PM:
            for ppl in PPL:
                for chl in CHL:
                    n = 85
                    coords2 = []
                    vip = []
                    mtx = []
                    last_coords = []
                    last_coords2 = []
                    population = []
                    st = []
                    dead_individuals = []
                    dict_populations = {}
                    way = []
                    stop = [0]
                    PERCENTAGE_OF_MUTATIONS = pm
                    NUMBER_OF_GENERATIONS = ng
                    POPULATIONS = ppl * n
                    CHILDREN = chl
                    itog = []
                    a = [[182, 111], [77, 104], [182, 90], [182, 102], [116, 166], [174, 140], [145, 125], [86, 59],
                         [83, 182], [131, 155], [140, 151], [144, 58], [12, 162], [112, 153], [172, 0], [39, 23],
                         [39, 167], [118, 91], [14, 80], [12, 70], [164, 24], [16, 187], [140, 119], [50, 58],
                         [189, 174], [110, 5], [114, 63], [115, 149], [94, 97], [161, 181], [129, 53], [126, 13],
                         [200, 125], [81, 185], [151, 5], [6, 128], [12, 3], [10, 28], [155, 139], [64, 11], [127, 190],
                         [8, 47], [124, 9], [124, 159], [172, 67], [131, 100], [80, 20], [109, 164], [53, 89],
                         [17, 155], [176, 107], [199, 115], [93, 175], [101, 1], [70, 133], [83, 143], [188, 32],
                         [53, 183], [154, 90], [47, 109], [9, 140], [155, 162], [5, 54], [127, 156], [155, 129],
                         [52, 191], [177, 156], [26, 90], [69, 127], [185, 33], [101, 36], [108, 86], [80, 5], [94, 3],
                         [115, 199], [113, 3], [145, 43], [174, 148], [17, 52], [61, 96], [122, 133], [40, 169],
                         [31, 187], [181, 120], [19, 72]]

                    for i in a:
                        # b = random.choice([0, 0])
                        # a = f'{random.randint(0, 200)} {random.randint(0, 200)}'
                        # print(a)
                        # list_point = list(map(int, a.split(' ')))
                        coords2.append(i[:2])
                        if len(i) == 3:
                            vip.append(i[:2])
                        else:
                            mtx.append(i)

                    if len(vip) != 0:
                        vip.insert(0, [0, 0])
                    else:
                        mtx.insert(0, [0, 0])
                    coords2.insert(0, [0, 0])

                    for _ in range(10):
                        # print('----------')
                        last_coords = []
                        last_coords2 = []
                        population = []
                        st = []
                        dead_individuals = []
                        dict_populations = {}
                        way = []
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
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

                                    child1[number1], child1[number2] = child1[number2], child1[number1]

                                    # мутация второго потомка
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

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

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                if list(dict_populations.values())[0] != stop[-1]:
                                    stop.clear()
                                    stop.append(list(dict_populations.values())[0])
                                else:
                                    stop.append(list(dict_populations.values())[0])

                                if len(stop) == 10000:
                                    break

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

                                if dict_populations[str(q1)] > dict_populations[
                                    str(q2)]:  # поиск победителя первого тура
                                    win1 = q2
                                else:
                                    win1 = q1

                                # 2 тур
                                qq1 = random.choice(population)  # первый участник
                                qq2 = random.choice(population)  # второй участник

                                if dict_populations[str(qq1)] > dict_populations[
                                    str(qq2)]:  # поиск победителя второго тура
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
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

                                    child1[number1], child1[number2] = child1[number2], child1[number1]

                                    # мутация второго потомка
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

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

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                if list(dict_populations.values())[0] != stop[-1]:
                                    stop.clear()
                                    stop.append(list(dict_populations.values())[0])
                                else:
                                    stop.append(list(dict_populations.values())[0])

                                if len(stop) == 10000:
                                    break

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
                            for i in range(NUMBER_OF_GENERATIONS):
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

                                if dict_populations[str(q1)] > dict_populations[
                                    str(q2)]:  # поиск победителя первого тура
                                    win1 = q2
                                    # dead_individuals.append(list(dict_populations)[-1])
                                else:
                                    win1 = q1

                                # 2 тур
                                qq1 = random.choice(population)  # первый участник
                                qq2 = random.choice(population)  # второй участник

                                if dict_populations[str(qq1)] > dict_populations[
                                    str(qq2)]:  # поиск победителя второго тура
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
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

                                    child1[number1], child1[number2] = child1[number2], child1[number1]

                                    # мутация второго потомка
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

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

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                if list(dict_populations.values())[0] != stop[-1]:
                                    stop.clear()
                                    stop.append(list(dict_populations.values())[0])
                                else:
                                    stop.append(list(dict_populations.values())[0])

                                if len(stop) == 10000:
                                    break

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

                        last_coords3 = []
                        # print(last_coords3)

                        for i in last_coords:
                            if i not in last_coords3:
                                last_coords3.append(i)

                        for i in last_coords2:
                            if i not in last_coords3:
                                last_coords3.append(i)

                        # print(sum(get_list_distance(last_coords3)))
                        itog.append(sum(get_list_distance(last_coords3)))
                    print()
                    print(f"{itog} ({sum(itog) / 10}), ng = {ng}, pm = {pm}, ppl = {ppl}, chl = {chl}")
def func3():
    NG = [150000]  # количество генераций
    PM = [25]  # процент мутаций
    PPL = [6]  # количество особей в популяции
    CHL = [1]  # количество точек разрыва

    k = 0
    for ng in NG:
        for pm in PM:
            for ppl in PPL:
                for chl in CHL:
                    n = 85
                    coords2 = []
                    vip = []
                    mtx = []
                    last_coords = []
                    last_coords2 = []
                    population = []
                    st = []
                    dead_individuals = []
                    dict_populations = {}
                    way = []
                    stop = [0]
                    PERCENTAGE_OF_MUTATIONS = pm
                    NUMBER_OF_GENERATIONS = ng
                    POPULATIONS = ppl * n
                    CHILDREN = chl
                    itog = []
                    a = [[182, 111], [77, 104], [182, 90], [182, 102], [116, 166], [174, 140], [145, 125], [86, 59],
                         [83, 182], [131, 155], [140, 151], [144, 58], [12, 162], [112, 153], [172, 0], [39, 23],
                         [39, 167], [118, 91], [14, 80], [12, 70], [164, 24], [16, 187], [140, 119], [50, 58],
                         [189, 174], [110, 5], [114, 63], [115, 149], [94, 97], [161, 181], [129, 53], [126, 13],
                         [200, 125], [81, 185], [151, 5], [6, 128], [12, 3], [10, 28], [155, 139], [64, 11], [127, 190],
                         [8, 47], [124, 9], [124, 159], [172, 67], [131, 100], [80, 20], [109, 164], [53, 89],
                         [17, 155], [176, 107], [199, 115], [93, 175], [101, 1], [70, 133], [83, 143], [188, 32],
                         [53, 183], [154, 90], [47, 109], [9, 140], [155, 162], [5, 54], [127, 156], [155, 129],
                         [52, 191], [177, 156], [26, 90], [69, 127], [185, 33], [101, 36], [108, 86], [80, 5], [94, 3],
                         [115, 199], [113, 3], [145, 43], [174, 148], [17, 52], [61, 96], [122, 133], [40, 169],
                         [31, 187], [181, 120], [19, 72]]

                    for i in a:
                        # b = random.choice([0, 0])
                        # a = f'{random.randint(0, 200)} {random.randint(0, 200)}'
                        # print(a)
                        # list_point = list(map(int, a.split(' ')))
                        coords2.append(i[:2])
                        if len(i) == 3:
                            vip.append(i[:2])
                        else:
                            mtx.append(i)

                    if len(vip) != 0:
                        vip.insert(0, [0, 0])
                    else:
                        mtx.insert(0, [0, 0])
                    coords2.insert(0, [0, 0])

                    for _ in range(10):
                        # print('----------')
                        last_coords = []
                        last_coords2 = []
                        population = []
                        st = []
                        dead_individuals = []
                        dict_populations = {}
                        way = []
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
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

                                    child1[number1], child1[number2] = child1[number2], child1[number1]

                                    # мутация второго потомка
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

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

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                if list(dict_populations.values())[0] != stop[-1]:
                                    stop.clear()
                                    stop.append(list(dict_populations.values())[0])
                                else:
                                    stop.append(list(dict_populations.values())[0])

                                if len(stop) == 10000:
                                    break

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

                                if dict_populations[str(q1)] > dict_populations[
                                    str(q2)]:  # поиск победителя первого тура
                                    win1 = q2
                                else:
                                    win1 = q1

                                # 2 тур
                                qq1 = random.choice(population)  # первый участник
                                qq2 = random.choice(population)  # второй участник

                                if dict_populations[str(qq1)] > dict_populations[
                                    str(qq2)]:  # поиск победителя второго тура
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
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

                                    child1[number1], child1[number2] = child1[number2], child1[number1]

                                    # мутация второго потомка
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

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

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                if list(dict_populations.values())[0] != stop[-1]:
                                    stop.clear()
                                    stop.append(list(dict_populations.values())[0])
                                else:
                                    stop.append(list(dict_populations.values())[0])

                                if len(stop) == 10000:
                                    break

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
                            for i in range(NUMBER_OF_GENERATIONS):
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

                                if dict_populations[str(q1)] > dict_populations[
                                    str(q2)]:  # поиск победителя первого тура
                                    win1 = q2
                                    # dead_individuals.append(list(dict_populations)[-1])
                                else:
                                    win1 = q1

                                # 2 тур
                                qq1 = random.choice(population)  # первый участник
                                qq2 = random.choice(population)  # второй участник

                                if dict_populations[str(qq1)] > dict_populations[
                                    str(qq2)]:  # поиск победителя второго тура
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
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

                                    child1[number1], child1[number2] = child1[number2], child1[number1]

                                    # мутация второго потомка
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

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

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                if list(dict_populations.values())[0] != stop[-1]:
                                    stop.clear()
                                    stop.append(list(dict_populations.values())[0])
                                else:
                                    stop.append(list(dict_populations.values())[0])

                                if len(stop) == 10000:
                                    break

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

                        last_coords3 = []
                        # print(last_coords3)

                        for i in last_coords:
                            if i not in last_coords3:
                                last_coords3.append(i)

                        for i in last_coords2:
                            if i not in last_coords3:
                                last_coords3.append(i)

                        # print(sum(get_list_distance(last_coords3)))
                        itog.append(sum(get_list_distance(last_coords3)))
                    print()
                    print(f"{itog} ({sum(itog) / 10}), ng = {ng}, pm = {pm}, ppl = {ppl}, chl = {chl}")


def func4():
    NG = [150000]  # количество генераций
    PM = [25]  # процент мутаций
    PPL = [6]  # количество особей в популяции
    CHL = [2]  # количество точек разрыва

    k = 0
    for ng in NG:
        for pm in PM:
            for ppl in PPL:
                for chl in CHL:
                    n = 85
                    coords2 = []
                    vip = []
                    mtx = []
                    last_coords = []
                    last_coords2 = []
                    population = []
                    st = []
                    dead_individuals = []
                    dict_populations = {}
                    way = []
                    stop = [0]
                    PERCENTAGE_OF_MUTATIONS = pm
                    NUMBER_OF_GENERATIONS = ng
                    POPULATIONS = ppl * n
                    CHILDREN = chl
                    itog = []
                    a = [[182, 111], [77, 104], [182, 90], [182, 102], [116, 166], [174, 140], [145, 125], [86, 59],
                         [83, 182], [131, 155], [140, 151], [144, 58], [12, 162], [112, 153], [172, 0], [39, 23],
                         [39, 167], [118, 91], [14, 80], [12, 70], [164, 24], [16, 187], [140, 119], [50, 58],
                         [189, 174], [110, 5], [114, 63], [115, 149], [94, 97], [161, 181], [129, 53], [126, 13],
                         [200, 125], [81, 185], [151, 5], [6, 128], [12, 3], [10, 28], [155, 139], [64, 11], [127, 190],
                         [8, 47], [124, 9], [124, 159], [172, 67], [131, 100], [80, 20], [109, 164], [53, 89],
                         [17, 155], [176, 107], [199, 115], [93, 175], [101, 1], [70, 133], [83, 143], [188, 32],
                         [53, 183], [154, 90], [47, 109], [9, 140], [155, 162], [5, 54], [127, 156], [155, 129],
                         [52, 191], [177, 156], [26, 90], [69, 127], [185, 33], [101, 36], [108, 86], [80, 5], [94, 3],
                         [115, 199], [113, 3], [145, 43], [174, 148], [17, 52], [61, 96], [122, 133], [40, 169],
                         [31, 187], [181, 120], [19, 72]]

                    for i in a:
                        # b = random.choice([0, 0])
                        # a = f'{random.randint(0, 200)} {random.randint(0, 200)}'
                        # print(a)
                        # list_point = list(map(int, a.split(' ')))
                        coords2.append(i[:2])
                        if len(i) == 3:
                            vip.append(i[:2])
                        else:
                            mtx.append(i)

                    if len(vip) != 0:
                        vip.insert(0, [0, 0])
                    else:
                        mtx.insert(0, [0, 0])
                    coords2.insert(0, [0, 0])

                    for _ in range(10):
                        # print('----------')
                        last_coords = []
                        last_coords2 = []
                        population = []
                        st = []
                        dead_individuals = []
                        dict_populations = {}
                        way = []
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
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

                                    child1[number1], child1[number2] = child1[number2], child1[number1]

                                    # мутация второго потомка
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

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

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                if list(dict_populations.values())[0] != stop[-1]:
                                    stop.clear()
                                    stop.append(list(dict_populations.values())[0])
                                else:
                                    stop.append(list(dict_populations.values())[0])

                                if len(stop) == 10000:
                                    break

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

                                if dict_populations[str(q1)] > dict_populations[
                                    str(q2)]:  # поиск победителя первого тура
                                    win1 = q2
                                else:
                                    win1 = q1

                                # 2 тур
                                qq1 = random.choice(population)  # первый участник
                                qq2 = random.choice(population)  # второй участник

                                if dict_populations[str(qq1)] > dict_populations[
                                    str(qq2)]:  # поиск победителя второго тура
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
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

                                    child1[number1], child1[number2] = child1[number2], child1[number1]

                                    # мутация второго потомка
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

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

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                if list(dict_populations.values())[0] != stop[-1]:
                                    stop.clear()
                                    stop.append(list(dict_populations.values())[0])
                                else:
                                    stop.append(list(dict_populations.values())[0])

                                if len(stop) == 10000:
                                    break

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
                            for i in range(NUMBER_OF_GENERATIONS):
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

                                if dict_populations[str(q1)] > dict_populations[
                                    str(q2)]:  # поиск победителя первого тура
                                    win1 = q2
                                    # dead_individuals.append(list(dict_populations)[-1])
                                else:
                                    win1 = q1

                                # 2 тур
                                qq1 = random.choice(population)  # первый участник
                                qq2 = random.choice(population)  # второй участник

                                if dict_populations[str(qq1)] > dict_populations[
                                    str(qq2)]:  # поиск победителя второго тура
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
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

                                    child1[number1], child1[number2] = child1[number2], child1[number1]

                                    # мутация второго потомка
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

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

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                if list(dict_populations.values())[0] != stop[-1]:
                                    stop.clear()
                                    stop.append(list(dict_populations.values())[0])
                                else:
                                    stop.append(list(dict_populations.values())[0])

                                if len(stop) == 10000:
                                    break

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

                        last_coords3 = []
                        # print(last_coords3)

                        for i in last_coords:
                            if i not in last_coords3:
                                last_coords3.append(i)

                        for i in last_coords2:
                            if i not in last_coords3:
                                last_coords3.append(i)

                        # print(sum(get_list_distance(last_coords3)))
                        itog.append(sum(get_list_distance(last_coords3)))
                    print()
                    print(f"{itog} ({sum(itog) / 10}), ng = {ng}, pm = {pm}, ppl = {ppl}, chl = {chl}")


def func5():
    NG = [150000]  # количество генераций
    PM = [50]  # процент мутаций
    PPL = [6]  # количество особей в популяции
    CHL = [1]  # количество точек разрыва

    k = 0
    for ng in NG:
        for pm in PM:
            for ppl in PPL:
                for chl in CHL:
                    n = 85
                    coords2 = []
                    vip = []
                    mtx = []
                    last_coords = []
                    last_coords2 = []
                    population = []
                    st = []
                    dead_individuals = []
                    dict_populations = {}
                    way = []
                    stop = [0]
                    PERCENTAGE_OF_MUTATIONS = pm
                    NUMBER_OF_GENERATIONS = ng
                    POPULATIONS = ppl * n
                    CHILDREN = chl
                    itog = []
                    a = [[182, 111], [77, 104], [182, 90], [182, 102], [116, 166], [174, 140], [145, 125], [86, 59],
                         [83, 182], [131, 155], [140, 151], [144, 58], [12, 162], [112, 153], [172, 0], [39, 23],
                         [39, 167], [118, 91], [14, 80], [12, 70], [164, 24], [16, 187], [140, 119], [50, 58],
                         [189, 174], [110, 5], [114, 63], [115, 149], [94, 97], [161, 181], [129, 53], [126, 13],
                         [200, 125], [81, 185], [151, 5], [6, 128], [12, 3], [10, 28], [155, 139], [64, 11], [127, 190],
                         [8, 47], [124, 9], [124, 159], [172, 67], [131, 100], [80, 20], [109, 164], [53, 89],
                         [17, 155], [176, 107], [199, 115], [93, 175], [101, 1], [70, 133], [83, 143], [188, 32],
                         [53, 183], [154, 90], [47, 109], [9, 140], [155, 162], [5, 54], [127, 156], [155, 129],
                         [52, 191], [177, 156], [26, 90], [69, 127], [185, 33], [101, 36], [108, 86], [80, 5], [94, 3],
                         [115, 199], [113, 3], [145, 43], [174, 148], [17, 52], [61, 96], [122, 133], [40, 169],
                         [31, 187], [181, 120], [19, 72]]

                    for i in a:
                        # b = random.choice([0, 0])
                        # a = f'{random.randint(0, 200)} {random.randint(0, 200)}'
                        # print(a)
                        # list_point = list(map(int, a.split(' ')))
                        coords2.append(i[:2])
                        if len(i) == 3:
                            vip.append(i[:2])
                        else:
                            mtx.append(i)

                    if len(vip) != 0:
                        vip.insert(0, [0, 0])
                    else:
                        mtx.insert(0, [0, 0])
                    coords2.insert(0, [0, 0])

                    for _ in range(10):
                        # print('----------')
                        last_coords = []
                        last_coords2 = []
                        population = []
                        st = []
                        dead_individuals = []
                        dict_populations = {}
                        way = []
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
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

                                    child1[number1], child1[number2] = child1[number2], child1[number1]

                                    # мутация второго потомка
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

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

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                if list(dict_populations.values())[0] != stop[-1]:
                                    stop.clear()
                                    stop.append(list(dict_populations.values())[0])
                                else:
                                    stop.append(list(dict_populations.values())[0])

                                if len(stop) == 10000:
                                    break

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

                                if dict_populations[str(q1)] > dict_populations[
                                    str(q2)]:  # поиск победителя первого тура
                                    win1 = q2
                                else:
                                    win1 = q1

                                # 2 тур
                                qq1 = random.choice(population)  # первый участник
                                qq2 = random.choice(population)  # второй участник

                                if dict_populations[str(qq1)] > dict_populations[
                                    str(qq2)]:  # поиск победителя второго тура
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
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

                                    child1[number1], child1[number2] = child1[number2], child1[number1]

                                    # мутация второго потомка
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

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

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                if list(dict_populations.values())[0] != stop[-1]:
                                    stop.clear()
                                    stop.append(list(dict_populations.values())[0])
                                else:
                                    stop.append(list(dict_populations.values())[0])

                                if len(stop) == 10000:
                                    break

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
                            for i in range(NUMBER_OF_GENERATIONS):
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

                                if dict_populations[str(q1)] > dict_populations[
                                    str(q2)]:  # поиск победителя первого тура
                                    win1 = q2
                                    # dead_individuals.append(list(dict_populations)[-1])
                                else:
                                    win1 = q1

                                # 2 тур
                                qq1 = random.choice(population)  # первый участник
                                qq2 = random.choice(population)  # второй участник

                                if dict_populations[str(qq1)] > dict_populations[
                                    str(qq2)]:  # поиск победителя второго тура
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
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

                                    child1[number1], child1[number2] = child1[number2], child1[number1]

                                    # мутация второго потомка
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

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

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                if list(dict_populations.values())[0] != stop[-1]:
                                    stop.clear()
                                    stop.append(list(dict_populations.values())[0])
                                else:
                                    stop.append(list(dict_populations.values())[0])

                                if len(stop) == 10000:
                                    break

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

                        last_coords3 = []
                        # print(last_coords3)

                        for i in last_coords:
                            if i not in last_coords3:
                                last_coords3.append(i)

                        for i in last_coords2:
                            if i not in last_coords3:
                                last_coords3.append(i)

                        # print(sum(get_list_distance(last_coords3)))
                        itog.append(sum(get_list_distance(last_coords3)))
                    print()
                    print(f"{itog} ({sum(itog) / 10}), ng = {ng}, pm = {pm}, ppl = {ppl}, chl = {chl}")


def func6():
    NG = [150000]  # количество генераций
    PM = [50]  # процент мутаций
    PPL = [6]  # количество особей в популяции
    CHL = [2]  # количество точек разрыва

    k = 0
    for ng in NG:
        for pm in PM:
            for ppl in PPL:
                for chl in CHL:
                    n = 85
                    coords2 = []
                    vip = []
                    mtx = []
                    last_coords = []
                    last_coords2 = []
                    population = []
                    st = []
                    dead_individuals = []
                    dict_populations = {}
                    way = []
                    stop = [0]
                    PERCENTAGE_OF_MUTATIONS = pm
                    NUMBER_OF_GENERATIONS = ng
                    POPULATIONS = ppl * n
                    CHILDREN = chl
                    itog = []
                    a = [[182, 111], [77, 104], [182, 90], [182, 102], [116, 166], [174, 140], [145, 125], [86, 59],
                         [83, 182], [131, 155], [140, 151], [144, 58], [12, 162], [112, 153], [172, 0], [39, 23],
                         [39, 167], [118, 91], [14, 80], [12, 70], [164, 24], [16, 187], [140, 119], [50, 58],
                         [189, 174], [110, 5], [114, 63], [115, 149], [94, 97], [161, 181], [129, 53], [126, 13],
                         [200, 125], [81, 185], [151, 5], [6, 128], [12, 3], [10, 28], [155, 139], [64, 11], [127, 190],
                         [8, 47], [124, 9], [124, 159], [172, 67], [131, 100], [80, 20], [109, 164], [53, 89],
                         [17, 155], [176, 107], [199, 115], [93, 175], [101, 1], [70, 133], [83, 143], [188, 32],
                         [53, 183], [154, 90], [47, 109], [9, 140], [155, 162], [5, 54], [127, 156], [155, 129],
                         [52, 191], [177, 156], [26, 90], [69, 127], [185, 33], [101, 36], [108, 86], [80, 5], [94, 3],
                         [115, 199], [113, 3], [145, 43], [174, 148], [17, 52], [61, 96], [122, 133], [40, 169],
                         [31, 187], [181, 120], [19, 72]]

                    for i in a:
                        # b = random.choice([0, 0])
                        # a = f'{random.randint(0, 200)} {random.randint(0, 200)}'
                        # print(a)
                        # list_point = list(map(int, a.split(' ')))
                        coords2.append(i[:2])
                        if len(i) == 3:
                            vip.append(i[:2])
                        else:
                            mtx.append(i)

                    if len(vip) != 0:
                        vip.insert(0, [0, 0])
                    else:
                        mtx.insert(0, [0, 0])
                    coords2.insert(0, [0, 0])

                    for _ in range(10):
                        # print('----------')
                        last_coords = []
                        last_coords2 = []
                        population = []
                        st = []
                        dead_individuals = []
                        dict_populations = {}
                        way = []
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
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

                                    child1[number1], child1[number2] = child1[number2], child1[number1]

                                    # мутация второго потомка
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

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

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                if list(dict_populations.values())[0] != stop[-1]:
                                    stop.clear()
                                    stop.append(list(dict_populations.values())[0])
                                else:
                                    stop.append(list(dict_populations.values())[0])

                                if len(stop) == 10000:
                                    break

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

                                if dict_populations[str(q1)] > dict_populations[
                                    str(q2)]:  # поиск победителя первого тура
                                    win1 = q2
                                else:
                                    win1 = q1

                                # 2 тур
                                qq1 = random.choice(population)  # первый участник
                                qq2 = random.choice(population)  # второй участник

                                if dict_populations[str(qq1)] > dict_populations[
                                    str(qq2)]:  # поиск победителя второго тура
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
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

                                    child1[number1], child1[number2] = child1[number2], child1[number1]

                                    # мутация второго потомка
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

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

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                if list(dict_populations.values())[0] != stop[-1]:
                                    stop.clear()
                                    stop.append(list(dict_populations.values())[0])
                                else:
                                    stop.append(list(dict_populations.values())[0])

                                if len(stop) == 10000:
                                    break

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
                            for i in range(NUMBER_OF_GENERATIONS):
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

                                if dict_populations[str(q1)] > dict_populations[
                                    str(q2)]:  # поиск победителя первого тура
                                    win1 = q2
                                    # dead_individuals.append(list(dict_populations)[-1])
                                else:
                                    win1 = q1

                                # 2 тур
                                qq1 = random.choice(population)  # первый участник
                                qq2 = random.choice(population)  # второй участник

                                if dict_populations[str(qq1)] > dict_populations[
                                    str(qq2)]:  # поиск победителя второго тура
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
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

                                    child1[number1], child1[number2] = child1[number2], child1[number1]

                                    # мутация второго потомка
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

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

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                if list(dict_populations.values())[0] != stop[-1]:
                                    stop.clear()
                                    stop.append(list(dict_populations.values())[0])
                                else:
                                    stop.append(list(dict_populations.values())[0])

                                if len(stop) == 10000:
                                    break

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

                        last_coords3 = []
                        # print(last_coords3)

                        for i in last_coords:
                            if i not in last_coords3:
                                last_coords3.append(i)

                        for i in last_coords2:
                            if i not in last_coords3:
                                last_coords3.append(i)

                        # print(sum(get_list_distance(last_coords3)))
                        itog.append(sum(get_list_distance(last_coords3)))
                    print()
                    print(f"{itog} ({sum(itog) / 10}), ng = {ng}, pm = {pm}, ppl = {ppl}, chl = {chl}")

def func7():
    NG = [150000]  # количество генераций
    PM = [75]  # процент мутаций
    PPL = [6]  # количество особей в популяции
    CHL = [1]  # количество точек разрыва

    k = 0
    for ng in NG:
        for pm in PM:
            for ppl in PPL:
                for chl in CHL:
                    n = 85
                    coords2 = []
                    vip = []
                    mtx = []
                    last_coords = []
                    last_coords2 = []
                    population = []
                    st = []
                    dead_individuals = []
                    dict_populations = {}
                    way = []
                    stop = [0]
                    PERCENTAGE_OF_MUTATIONS = pm
                    NUMBER_OF_GENERATIONS = ng
                    POPULATIONS = ppl * n
                    CHILDREN = chl
                    itog = []
                    a = [[182, 111], [77, 104], [182, 90], [182, 102], [116, 166], [174, 140], [145, 125], [86, 59],
                         [83, 182], [131, 155], [140, 151], [144, 58], [12, 162], [112, 153], [172, 0], [39, 23],
                         [39, 167], [118, 91], [14, 80], [12, 70], [164, 24], [16, 187], [140, 119], [50, 58],
                         [189, 174], [110, 5], [114, 63], [115, 149], [94, 97], [161, 181], [129, 53], [126, 13],
                         [200, 125], [81, 185], [151, 5], [6, 128], [12, 3], [10, 28], [155, 139], [64, 11], [127, 190],
                         [8, 47], [124, 9], [124, 159], [172, 67], [131, 100], [80, 20], [109, 164], [53, 89],
                         [17, 155], [176, 107], [199, 115], [93, 175], [101, 1], [70, 133], [83, 143], [188, 32],
                         [53, 183], [154, 90], [47, 109], [9, 140], [155, 162], [5, 54], [127, 156], [155, 129],
                         [52, 191], [177, 156], [26, 90], [69, 127], [185, 33], [101, 36], [108, 86], [80, 5], [94, 3],
                         [115, 199], [113, 3], [145, 43], [174, 148], [17, 52], [61, 96], [122, 133], [40, 169],
                         [31, 187], [181, 120], [19, 72]]

                    for i in a:
                        # b = random.choice([0, 0])
                        # a = f'{random.randint(0, 200)} {random.randint(0, 200)}'
                        # print(a)
                        # list_point = list(map(int, a.split(' ')))
                        coords2.append(i[:2])
                        if len(i) == 3:
                            vip.append(i[:2])
                        else:
                            mtx.append(i)

                    if len(vip) != 0:
                        vip.insert(0, [0, 0])
                    else:
                        mtx.insert(0, [0, 0])
                    coords2.insert(0, [0, 0])

                    for _ in range(10):
                        # print('----------')
                        last_coords = []
                        last_coords2 = []
                        population = []
                        st = []
                        dead_individuals = []
                        dict_populations = {}
                        way = []
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
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

                                    child1[number1], child1[number2] = child1[number2], child1[number1]

                                    # мутация второго потомка
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

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

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                if list(dict_populations.values())[0] != stop[-1]:
                                    stop.clear()
                                    stop.append(list(dict_populations.values())[0])
                                else:
                                    stop.append(list(dict_populations.values())[0])

                                if len(stop) == 10000:
                                    break

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

                                if dict_populations[str(q1)] > dict_populations[
                                    str(q2)]:  # поиск победителя первого тура
                                    win1 = q2
                                else:
                                    win1 = q1

                                # 2 тур
                                qq1 = random.choice(population)  # первый участник
                                qq2 = random.choice(population)  # второй участник

                                if dict_populations[str(qq1)] > dict_populations[
                                    str(qq2)]:  # поиск победителя второго тура
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
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

                                    child1[number1], child1[number2] = child1[number2], child1[number1]

                                    # мутация второго потомка
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

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

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                if list(dict_populations.values())[0] != stop[-1]:
                                    stop.clear()
                                    stop.append(list(dict_populations.values())[0])
                                else:
                                    stop.append(list(dict_populations.values())[0])

                                if len(stop) == 10000:
                                    break

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
                            for i in range(NUMBER_OF_GENERATIONS):
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

                                if dict_populations[str(q1)] > dict_populations[
                                    str(q2)]:  # поиск победителя первого тура
                                    win1 = q2
                                    # dead_individuals.append(list(dict_populations)[-1])
                                else:
                                    win1 = q1

                                # 2 тур
                                qq1 = random.choice(population)  # первый участник
                                qq2 = random.choice(population)  # второй участник

                                if dict_populations[str(qq1)] > dict_populations[
                                    str(qq2)]:  # поиск победителя второго тура
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
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

                                    child1[number1], child1[number2] = child1[number2], child1[number1]

                                    # мутация второго потомка
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

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

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                if list(dict_populations.values())[0] != stop[-1]:
                                    stop.clear()
                                    stop.append(list(dict_populations.values())[0])
                                else:
                                    stop.append(list(dict_populations.values())[0])

                                if len(stop) == 10000:
                                    break

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

                        last_coords3 = []
                        # print(last_coords3)

                        for i in last_coords:
                            if i not in last_coords3:
                                last_coords3.append(i)

                        for i in last_coords2:
                            if i not in last_coords3:
                                last_coords3.append(i)

                        # print(sum(get_list_distance(last_coords3)))
                        itog.append(sum(get_list_distance(last_coords3)))
                    print()
                    print(f"{itog} ({sum(itog) / 10}), ng = {ng}, pm = {pm}, ppl = {ppl}, chl = {chl}")

def func8():
    NG = [150000]  # количество генераций
    PM = [75]  # процент мутаций
    PPL = [6]  # количество особей в популяции
    CHL = [2]  # количество точек разрыва

    k = 0
    for ng in NG:
        for pm in PM:
            for ppl in PPL:
                for chl in CHL:
                    n = 85
                    coords2 = []
                    vip = []
                    mtx = []
                    last_coords = []
                    last_coords2 = []
                    population = []
                    st = []
                    dead_individuals = []
                    dict_populations = {}
                    way = []
                    stop = [0]
                    PERCENTAGE_OF_MUTATIONS = pm
                    NUMBER_OF_GENERATIONS = ng
                    POPULATIONS = ppl * n
                    CHILDREN = chl
                    itog = []
                    a = [[182, 111], [77, 104], [182, 90], [182, 102], [116, 166], [174, 140], [145, 125], [86, 59],
                         [83, 182], [131, 155], [140, 151], [144, 58], [12, 162], [112, 153], [172, 0], [39, 23],
                         [39, 167], [118, 91], [14, 80], [12, 70], [164, 24], [16, 187], [140, 119], [50, 58],
                         [189, 174], [110, 5], [114, 63], [115, 149], [94, 97], [161, 181], [129, 53], [126, 13],
                         [200, 125], [81, 185], [151, 5], [6, 128], [12, 3], [10, 28], [155, 139], [64, 11], [127, 190],
                         [8, 47], [124, 9], [124, 159], [172, 67], [131, 100], [80, 20], [109, 164], [53, 89],
                         [17, 155], [176, 107], [199, 115], [93, 175], [101, 1], [70, 133], [83, 143], [188, 32],
                         [53, 183], [154, 90], [47, 109], [9, 140], [155, 162], [5, 54], [127, 156], [155, 129],
                         [52, 191], [177, 156], [26, 90], [69, 127], [185, 33], [101, 36], [108, 86], [80, 5], [94, 3],
                         [115, 199], [113, 3], [145, 43], [174, 148], [17, 52], [61, 96], [122, 133], [40, 169],
                         [31, 187], [181, 120], [19, 72]]

                    for i in a:
                        # b = random.choice([0, 0])
                        # a = f'{random.randint(0, 200)} {random.randint(0, 200)}'
                        # print(a)
                        # list_point = list(map(int, a.split(' ')))
                        coords2.append(i[:2])
                        if len(i) == 3:
                            vip.append(i[:2])
                        else:
                            mtx.append(i)

                    if len(vip) != 0:
                        vip.insert(0, [0, 0])
                    else:
                        mtx.insert(0, [0, 0])
                    coords2.insert(0, [0, 0])

                    for _ in range(10):
                        # print('----------')
                        last_coords = []
                        last_coords2 = []
                        population = []
                        st = []
                        dead_individuals = []
                        dict_populations = {}
                        way = []
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
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

                                    child1[number1], child1[number2] = child1[number2], child1[number1]

                                    # мутация второго потомка
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

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

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                if list(dict_populations.values())[0] != stop[-1]:
                                    stop.clear()
                                    stop.append(list(dict_populations.values())[0])
                                else:
                                    stop.append(list(dict_populations.values())[0])

                                if len(stop) == 10000:
                                    break

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

                                if dict_populations[str(q1)] > dict_populations[
                                    str(q2)]:  # поиск победителя первого тура
                                    win1 = q2
                                else:
                                    win1 = q1

                                # 2 тур
                                qq1 = random.choice(population)  # первый участник
                                qq2 = random.choice(population)  # второй участник

                                if dict_populations[str(qq1)] > dict_populations[
                                    str(qq2)]:  # поиск победителя второго тура
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
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

                                    child1[number1], child1[number2] = child1[number2], child1[number1]

                                    # мутация второго потомка
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

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

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                if list(dict_populations.values())[0] != stop[-1]:
                                    stop.clear()
                                    stop.append(list(dict_populations.values())[0])
                                else:
                                    stop.append(list(dict_populations.values())[0])

                                if len(stop) == 10000:
                                    break

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
                            for i in range(NUMBER_OF_GENERATIONS):
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

                                if dict_populations[str(q1)] > dict_populations[
                                    str(q2)]:  # поиск победителя первого тура
                                    win1 = q2
                                    # dead_individuals.append(list(dict_populations)[-1])
                                else:
                                    win1 = q1

                                # 2 тур
                                qq1 = random.choice(population)  # первый участник
                                qq2 = random.choice(population)  # второй участник

                                if dict_populations[str(qq1)] > dict_populations[
                                    str(qq2)]:  # поиск победителя второго тура
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
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

                                    child1[number1], child1[number2] = child1[number2], child1[number1]

                                    # мутация второго потомка
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

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

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                if list(dict_populations.values())[0] != stop[-1]:
                                    stop.clear()
                                    stop.append(list(dict_populations.values())[0])
                                else:
                                    stop.append(list(dict_populations.values())[0])

                                if len(stop) == 10000:
                                    break

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

                        last_coords3 = []
                        # print(last_coords3)

                        for i in last_coords:
                            if i not in last_coords3:
                                last_coords3.append(i)

                        for i in last_coords2:
                            if i not in last_coords3:
                                last_coords3.append(i)

                        # print(sum(get_list_distance(last_coords3)))
                        itog.append(sum(get_list_distance(last_coords3)))
                    print()
                    print(f"{itog} ({sum(itog) / 10}), ng = {ng}, pm = {pm}, ppl = {ppl}, chl = {chl}")

def func9():
    NG = [150000]  # количество генераций
    PM = [90]  # процент мутаций
    PPL = [6]  # количество особей в популяции
    CHL = [1]  # количество точек разрыва

    k = 0
    for ng in NG:
        for pm in PM:
            for ppl in PPL:
                for chl in CHL:
                    n = 85
                    coords2 = []
                    vip = []
                    mtx = []
                    last_coords = []
                    last_coords2 = []
                    population = []
                    st = []
                    dead_individuals = []
                    dict_populations = {}
                    way = []
                    stop = [0]
                    PERCENTAGE_OF_MUTATIONS = pm
                    NUMBER_OF_GENERATIONS = ng
                    POPULATIONS = ppl * n
                    CHILDREN = chl
                    itog = []
                    a = [[182, 111], [77, 104], [182, 90], [182, 102], [116, 166], [174, 140], [145, 125], [86, 59],
                         [83, 182], [131, 155], [140, 151], [144, 58], [12, 162], [112, 153], [172, 0], [39, 23],
                         [39, 167], [118, 91], [14, 80], [12, 70], [164, 24], [16, 187], [140, 119], [50, 58],
                         [189, 174], [110, 5], [114, 63], [115, 149], [94, 97], [161, 181], [129, 53], [126, 13],
                         [200, 125], [81, 185], [151, 5], [6, 128], [12, 3], [10, 28], [155, 139], [64, 11], [127, 190],
                         [8, 47], [124, 9], [124, 159], [172, 67], [131, 100], [80, 20], [109, 164], [53, 89],
                         [17, 155], [176, 107], [199, 115], [93, 175], [101, 1], [70, 133], [83, 143], [188, 32],
                         [53, 183], [154, 90], [47, 109], [9, 140], [155, 162], [5, 54], [127, 156], [155, 129],
                         [52, 191], [177, 156], [26, 90], [69, 127], [185, 33], [101, 36], [108, 86], [80, 5], [94, 3],
                         [115, 199], [113, 3], [145, 43], [174, 148], [17, 52], [61, 96], [122, 133], [40, 169],
                         [31, 187], [181, 120], [19, 72]]

                    for i in a:
                        # b = random.choice([0, 0])
                        # a = f'{random.randint(0, 200)} {random.randint(0, 200)}'
                        # print(a)
                        # list_point = list(map(int, a.split(' ')))
                        coords2.append(i[:2])
                        if len(i) == 3:
                            vip.append(i[:2])
                        else:
                            mtx.append(i)

                    if len(vip) != 0:
                        vip.insert(0, [0, 0])
                    else:
                        mtx.insert(0, [0, 0])
                    coords2.insert(0, [0, 0])

                    for _ in range(10):
                        # print('----------')
                        last_coords = []
                        last_coords2 = []
                        population = []
                        st = []
                        dead_individuals = []
                        dict_populations = {}
                        way = []
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
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

                                    child1[number1], child1[number2] = child1[number2], child1[number1]

                                    # мутация второго потомка
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

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

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                if list(dict_populations.values())[0] != stop[-1]:
                                    stop.clear()
                                    stop.append(list(dict_populations.values())[0])
                                else:
                                    stop.append(list(dict_populations.values())[0])

                                if len(stop) == 10000:
                                    break

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

                                if dict_populations[str(q1)] > dict_populations[
                                    str(q2)]:  # поиск победителя первого тура
                                    win1 = q2
                                else:
                                    win1 = q1

                                # 2 тур
                                qq1 = random.choice(population)  # первый участник
                                qq2 = random.choice(population)  # второй участник

                                if dict_populations[str(qq1)] > dict_populations[
                                    str(qq2)]:  # поиск победителя второго тура
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
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

                                    child1[number1], child1[number2] = child1[number2], child1[number1]

                                    # мутация второго потомка
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

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

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                if list(dict_populations.values())[0] != stop[-1]:
                                    stop.clear()
                                    stop.append(list(dict_populations.values())[0])
                                else:
                                    stop.append(list(dict_populations.values())[0])

                                if len(stop) == 10000:
                                    break

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
                            for i in range(NUMBER_OF_GENERATIONS):
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

                                if dict_populations[str(q1)] > dict_populations[
                                    str(q2)]:  # поиск победителя первого тура
                                    win1 = q2
                                    # dead_individuals.append(list(dict_populations)[-1])
                                else:
                                    win1 = q1

                                # 2 тур
                                qq1 = random.choice(population)  # первый участник
                                qq2 = random.choice(population)  # второй участник

                                if dict_populations[str(qq1)] > dict_populations[
                                    str(qq2)]:  # поиск победителя второго тура
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
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

                                    child1[number1], child1[number2] = child1[number2], child1[number1]

                                    # мутация второго потомка
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

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

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                if list(dict_populations.values())[0] != stop[-1]:
                                    stop.clear()
                                    stop.append(list(dict_populations.values())[0])
                                else:
                                    stop.append(list(dict_populations.values())[0])

                                if len(stop) == 10000:
                                    break

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

                        last_coords3 = []
                        # print(last_coords3)

                        for i in last_coords:
                            if i not in last_coords3:
                                last_coords3.append(i)

                        for i in last_coords2:
                            if i not in last_coords3:
                                last_coords3.append(i)

                        # print(sum(get_list_distance(last_coords3)))
                        itog.append(sum(get_list_distance(last_coords3)))
                    print()
                    print(f"{itog} ({sum(itog) / 10}), ng = {ng}, pm = {pm}, ppl = {ppl}, chl = {chl}")


def func10():
    NG = [150000]  # количество генераций
    PM = [90]  # процент мутаций
    PPL = [6]  # количество особей в популяции
    CHL = [2]  # количество точек разрыва

    k = 0
    for ng in NG:
        for pm in PM:
            for ppl in PPL:
                for chl in CHL:
                    n = 85
                    coords2 = []
                    vip = []
                    mtx = []
                    last_coords = []
                    last_coords2 = []
                    population = []
                    st = []
                    dead_individuals = []
                    dict_populations = {}
                    way = []
                    stop = [0]
                    PERCENTAGE_OF_MUTATIONS = pm
                    NUMBER_OF_GENERATIONS = ng
                    POPULATIONS = ppl * n
                    CHILDREN = chl
                    itog = []
                    a = [[182, 111], [77, 104], [182, 90], [182, 102], [116, 166], [174, 140], [145, 125], [86, 59],
                         [83, 182], [131, 155], [140, 151], [144, 58], [12, 162], [112, 153], [172, 0], [39, 23],
                         [39, 167], [118, 91], [14, 80], [12, 70], [164, 24], [16, 187], [140, 119], [50, 58],
                         [189, 174], [110, 5], [114, 63], [115, 149], [94, 97], [161, 181], [129, 53], [126, 13],
                         [200, 125], [81, 185], [151, 5], [6, 128], [12, 3], [10, 28], [155, 139], [64, 11], [127, 190],
                         [8, 47], [124, 9], [124, 159], [172, 67], [131, 100], [80, 20], [109, 164], [53, 89],
                         [17, 155], [176, 107], [199, 115], [93, 175], [101, 1], [70, 133], [83, 143], [188, 32],
                         [53, 183], [154, 90], [47, 109], [9, 140], [155, 162], [5, 54], [127, 156], [155, 129],
                         [52, 191], [177, 156], [26, 90], [69, 127], [185, 33], [101, 36], [108, 86], [80, 5], [94, 3],
                         [115, 199], [113, 3], [145, 43], [174, 148], [17, 52], [61, 96], [122, 133], [40, 169],
                         [31, 187], [181, 120], [19, 72]]

                    for i in a:
                        # b = random.choice([0, 0])
                        # a = f'{random.randint(0, 200)} {random.randint(0, 200)}'
                        # print(a)
                        # list_point = list(map(int, a.split(' ')))
                        coords2.append(i[:2])
                        if len(i) == 3:
                            vip.append(i[:2])
                        else:
                            mtx.append(i)

                    if len(vip) != 0:
                        vip.insert(0, [0, 0])
                    else:
                        mtx.insert(0, [0, 0])
                    coords2.insert(0, [0, 0])

                    for _ in range(10):
                        # print('----------')
                        last_coords = []
                        last_coords2 = []
                        population = []
                        st = []
                        dead_individuals = []
                        dict_populations = {}
                        way = []
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
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

                                    child1[number1], child1[number2] = child1[number2], child1[number1]

                                    # мутация второго потомка
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

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

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                if list(dict_populations.values())[0] != stop[-1]:
                                    stop.clear()
                                    stop.append(list(dict_populations.values())[0])
                                else:
                                    stop.append(list(dict_populations.values())[0])

                                if len(stop) == 10000:
                                    break

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

                                if dict_populations[str(q1)] > dict_populations[
                                    str(q2)]:  # поиск победителя первого тура
                                    win1 = q2
                                else:
                                    win1 = q1

                                # 2 тур
                                qq1 = random.choice(population)  # первый участник
                                qq2 = random.choice(population)  # второй участник

                                if dict_populations[str(qq1)] > dict_populations[
                                    str(qq2)]:  # поиск победителя второго тура
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
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

                                    child1[number1], child1[number2] = child1[number2], child1[number1]

                                    # мутация второго потомка
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

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

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                dead_individuals.append(list(dict_populations)[-1])
                                dict_populations.pop(list(dict_populations)[-1])

                                if list(dict_populations.values())[0] != stop[-1]:
                                    stop.clear()
                                    stop.append(list(dict_populations.values())[0])
                                else:
                                    stop.append(list(dict_populations.values())[0])

                                if len(stop) == 10000:
                                    break

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
                            for i in range(NUMBER_OF_GENERATIONS):
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

                                if dict_populations[str(q1)] > dict_populations[
                                    str(q2)]:  # поиск победителя первого тура
                                    win1 = q2
                                    # dead_individuals.append(list(dict_populations)[-1])
                                else:
                                    win1 = q1

                                # 2 тур
                                qq1 = random.choice(population)  # первый участник
                                qq2 = random.choice(population)  # второй участник

                                if dict_populations[str(qq1)] > dict_populations[
                                    str(qq2)]:  # поиск победителя второго тура
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
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

                                    child1[number1], child1[number2] = child1[number2], child1[number1]

                                    # мутация второго потомка
                                    number1 = random.randint(1, n)
                                    number2 = random.randint(1, n)

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

                        last_coords3 = []
                        # print(last_coords3)

                        for i in last_coords:
                            if i not in last_coords3:
                                last_coords3.append(i)

                        for i in last_coords2:
                            if i not in last_coords3:
                                last_coords3.append(i)

                        # print(sum(get_list_distance(last_coords3)))
                        itog.append(sum(get_list_distance(last_coords3)))
                    print()
                    print(f"{itog} ({sum(itog) / 10}), ng = {ng}, pm = {pm}, ppl = {ppl}, chl = {chl}")


if __name__ == "__main__":
    p1 = Process(target=func1)
    p1.start()
    p2 = Process(target=func2)
    p2.start()
    p3 = Process(target=func3)
    p3.start()
    p4 = Process(target=func4)
    p4.start()
    p5 = Process(target=func5)
    p5.start()
    p6 = Process(target=func6)
    p6.start()
    p7 = Process(target=func7)
    p7.start()
    p8 = Process(target=func8)
    p8.start()
    p9 = Process(target=func9)
    p9.start()
    p10 = Process(target=func10)
    p10.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
    p9.join()
    p10.join()