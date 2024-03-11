# try:
import itertools
import time
import random
from copy import copy

import numpy as np
import pandas as pd
# import serial as serial
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from matplotlib import pyplot as plt
from python_tsp.heuristics import solve_tsp_local_search
from scipy.spatial import distance_matrix

import x
import y
from choise_metod import checkboxs
from distance_calculation import get_list_distance

# except Exception:
#     import os
#
#     os.system('pip install -r requirements.txt')
#     os.system('pip install python-tsp')

ONGR = [False]
ONR = [False]
coords_view = []
COORDS = []
METOD = [0]


class Demo(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "DeepPurple"
        self.screen = Screen()

        self.label = MDLabel(text="Пока никуда не едет(", pos_hint={'center_x': 0.52, 'center_y': 0.04},
                             font_style="Subtitle1")

        self.label1 = MDLabel(text="Полный перебор", pos_hint={'center_x': 1.17, 'center_y': 0.8},
                              font_style="Subtitle1")
        self.label2 = MDLabel(text="Жадный алгоритм", pos_hint={'center_x': 1.17, 'center_y': 0.7},
                              font_style="Subtitle1")
        self.label5 = MDLabel(text="Метод ветвей и границ", pos_hint={'center_x': 1.17, 'center_y': 0.6},
                              font_style="Subtitle1")
        self.label8 = MDLabel(text="Метод Монте-Карло", pos_hint={'center_x': 1.17, 'center_y': 0.5},
                              font_style="Subtitle1")
        self.label9 = MDLabel(text="Генетический алгоритм", pos_hint={'center_x': 1.17, 'center_y': 0.4},
                              font_style="Subtitle1")

        self.label7 = MDLabel(text="Приоритетный город", pos_hint={'center_x': 0.56, 'center_y': 0.6},
                              font_style="Subtitle1")

        self.label3 = MDLabel(text="Введите координаты:", pos_hint={'center_x': 0.65, 'center_y': 0.93},
                              font_style="Subtitle1")
        self.label4 = MDLabel(text="Выберите алгоритм решения:", pos_hint={'center_x': 1.08, 'center_y': 0.93},
                              font_style="Subtitle1")

        green = MDRectangleFlatButton(text="Добавить", pos_hint={'center_x': 0.15, 'center_y': 0.4},
                                      on_release=self.greenf, ripple_color='orange', line_color="orange")
        delite = MDRectangleFlatButton(text="Очистить", pos_hint={'center_x': 0.35, 'center_y': 0.4},
                                       on_release=self.delite, ripple_color='red', line_color="red")
        red = MDRectangleFlatButton(text="Старт", pos_hint={'center_x': 0.5, 'center_y': 0.1}, on_release=self.redf,
                                    ripple_color='green', line_color="green")

        sample1 = MDRectangleFlatButton(text="Тестовые данные №1", pos_hint={'center_x': 0.2, 'center_y': 0.3},
                                        on_release=self.sample1, ripple_color='pink', line_color="pink")
        sample2 = MDRectangleFlatButton(text="Тестовые данные №2", pos_hint={'center_x': 0.5, 'center_y': 0.3},
                                        on_release=self.sample2, ripple_color='blue', line_color="blue")
        sample3 = MDRectangleFlatButton(text="Рандомные данные", pos_hint={'center_x': 0.8, 'center_y': 0.3},
                                        on_release=self.sample3, ripple_color='purple', line_color="purple")
        sample4 = MDRectangleFlatButton(text="Рандомные данные без приоритетных городов", pos_hint={'center_x': 0.5, 'center_y': 0.22},
                                        on_release=self.sample4, ripple_color='brown', line_color="brown")

        self.x = Builder.load_string(x.x_input)
        self.y = Builder.load_string(y.y_input)

        checkbox = Builder.load_string(checkboxs)

        self.title = "Решение задачи коммивояжёра"
        self.screen.add_widget(green)
        self.screen.add_widget(red)
        self.screen.add_widget(delite)
        self.screen.add_widget(sample1)
        self.screen.add_widget(sample2)
        self.screen.add_widget(sample3)
        self.screen.add_widget(sample4)
        self.screen.add_widget(self.label)
        self.screen.add_widget(self.label1)
        self.screen.add_widget(self.label2)
        self.screen.add_widget(self.label3)
        self.screen.add_widget(self.label4)
        self.screen.add_widget(self.label5)
        self.screen.add_widget(self.label7)
        self.screen.add_widget(self.label8)
        self.screen.add_widget(self.label9)
        self.screen.add_widget(self.x)
        self.screen.add_widget(self.y)
        self.screen.add_widget(checkbox)

        # adding widgets to screen

        return self.screen

    def greenf(self, obj):
        if METOD[0] != 4:
            coords_view.append(f'({int(self.x.text)};{int(self.y.text)})')
            COORDS.append([int(self.x.text), int(self.y.text)])
            if len(coords_view) > 12:
                self.label.text = ', '.join(coords_view[:12]) + '...'
                self.x.text = ''
                self.y.text = ''
            else:
                self.label.text = ', '.join(coords_view)
                self.x.text = ''
                self.y.text = ''
        else:
            coords_view.append(f'({int(self.x.text)};{int(self.y.text)};1)')
            COORDS.append([int(self.x.text), int(self.y.text), 1])
            if len(coords_view) > 12:
                self.label.text = ', '.join(coords_view[:12]) + '...'
                self.x.text = ''
                self.y.text = ''
            else:
                self.label.text = ', '.join(coords_view)
                self.x.text = ''
                self.y.text = ''
    def sample1(self, obj):
        coords_view.append('(4;9)')
        coords_view.append('(6;2;1)')
        coords_view.append('(5;7;1)')
        coords_view.append('(6;1)')
        coords_view.append('(6;9)')

        COORDS.append([4, 9])
        COORDS.append([6, 2, 1])
        COORDS.append([5, 7, 1])
        COORDS.append([6, 1])
        COORDS.append([6, 9])
        if len(coords_view) > 12:
            self.label.text = ', '.join(coords_view[:12]) + '...'
            self.x.text = ''
            self.y.text = ''
        else:
            self.label.text = ', '.join(coords_view)
            self.x.text = ''
            self.y.text = ''

    def sample2(self, obj):
        coords_view.append('(2;0)')
        coords_view.append('(5;2)')
        coords_view.append('(6;4;1)')
        coords_view.append('(8;7)')
        coords_view.append('(6;9;1)')
        coords_view.append('(5;6)')
        coords_view.append('(3;3)')

        COORDS.append([2, 0])
        COORDS.append([5, 2])
        COORDS.append([6, 4, 1])
        COORDS.append([8, 7])
        COORDS.append([6, 9, 1])
        COORDS.append([5, 6])
        COORDS.append([3, 3])

        self.label.text = ', '.join(coords_view)
        self.x.text = ''
        self.y.text = ''

    def sample3(self, obj):
        a = random.randint(5, 60)
        # a = 1024
        print(a)
        for i in range(a):
            b = random.choice([0, 1])
            c = random.randint(0, 200)
            d = random.randint(0, 200)
            if b == 1:
                COORDS.append([c, d, 1])
                coords_view.append(f'{c};{d};1')
                print(c, d, 1)
            else:
                COORDS.append([c, d])
                coords_view.append(f'{c};{d}')
                print(c, d)

        if len(coords_view) > 12:
            self.label.text = ', '.join(coords_view[:12]) + '...'
            self.x.text = ''
            self.y.text = ''
        else:
            self.label.text = ', '.join(coords_view)
            self.x.text = ''
            self.y.text = ''

    def sample4(self, obj):
        a = random.randint(5, 60)
        print(a)
        for i in range(a):
            c = random.randint(0, 200)
            d = random.randint(0, 200)
            COORDS.append([c, d])
            coords_view.append(f'{c};{d}')
            print(c, d)

        if len(coords_view) > 12:
            self.label.text = ', '.join(coords_view[:12]) + '...'
            self.x.text = ''
            self.y.text = ''
        else:
            self.label.text = ', '.join(coords_view)
            self.x.text = ''
            self.y.text = ''
    def delite(self, obj):
        coords_view.clear()
        COORDS.clear()
        self.label.text = 'Пока никуда не едет('
        self.x.text = ''
        self.y.text = ''

    def redf(self, obj):
        print(COORDS)
        if len(COORDS) == 0:
            self.dialog = MDDialog(title='Введите координаты!',
                                   size_hint=(0.4, 0),
                                   buttons=[MDFlatButton(text='Закрыть', on_release=self.close_dialog)]
                                   )
            self.dialog.open()

        elif METOD[0] == 2:
            print('жадный алгоритм')
            if [0, 0] in COORDS:
                COORDS.remove([0, 0])
                # coords_view.remove('(0;0)')
            list_points = []
            way_now = {}
            shortest_way = 0
            town = 0
            shortest_way_coords = [[0, 0]]
            shortest_way_coords2 = []
            mtx = []
            vip = []
            result = []
            coords2 = []

            for i in COORDS:
                # a = f'{random.randint(0, 100)} {random.randint(0, 100)}'
                list_point = i
                coords2.append(list_point[:2])
                if len(list_point) == 3:
                    vip.append(list_point[:2])
                else:
                    mtx.append(list_point)

            if len(vip) != 0:
                vip.insert(0, [0, 0])
            else:
                mtx.insert(0, [0, 0])
            coords2.insert(0, (0, 0))

            fig, ax = plt.subplots()

            for i in coords2:
                if i not in vip:
                    if i[0] == 0 and i[1] == 0:
                        ax.add_patch(plt.Circle((i[0], i[1]), 0.3, facecolor='#FF0000', alpha=1))
                    else:
                        ax.add_patch(plt.Circle((i[0], i[1]), 0.3, facecolor='#9ebcda', alpha=1))

                    # plt.text(i[0] - 0.12, i[1] - 0.12, f'{town}')
                    town += 1

                else:
                    if i[0] == 0 and i[1] == 0:
                        ax.add_patch(plt.Circle((i[0], i[1]), 0.4, facecolor='#FF0000', alpha=1))
                    else:
                        ax.add_patch(plt.Circle((i[0], i[1]), 0.4, facecolor='#FF8C00', alpha=1))

                    # plt.text(i[0] - 0.12, i[1] - 0.12, f'{town}')
                    town += 1
            # del coords[0]
            if len(vip) != 0:
                while len(vip) > 2:
                    for i in range(len(vip)):
                        if i != 0:
                            list_points.append(vip[0])
                            list_points.append(vip[i])
                            distance = get_list_distance(list_points)
                            distance = distance[0]
                            way_now[i] = distance
                            # print(distance)
                            list_points.clear()
                    d = [k for k, v in way_now.items() if v == min(way_now.values())]
                    shortest_way += way_now[d[0]]
                    shortest_way_coords.append(vip[d[0]])
                    vip.insert(0, vip.pop(d[0]))
                    del vip[1]
                    way_now.clear()
                    # print(coords)

                distance = get_list_distance(vip)
                distance = distance[0]
                shortest_way += distance
                shortest_way_coords.append(vip[-1])
                # shortest_way_coords = shortest_way_coords.reverse()
                for i in shortest_way_coords:
                    result.append(i)

            shortest_way = 0
            distance = 0
            way_now = {}
            print('..........')

            # print(coords)
            mtx.insert(0, shortest_way_coords[-1])

            while len(mtx) > 2:
                for i in range(len(mtx)):
                    if i != 0:
                        list_points.append(mtx[0])
                        list_points.append(mtx[i])
                        distance = get_list_distance(list_points)
                        distance = distance[0]
                        way_now[i] = distance
                        # print(distance)
                        list_points.clear()
                d = [k for k, v in way_now.items() if v == min(way_now.values())]
                shortest_way += way_now[d[0]]
                shortest_way_coords2.append(mtx[d[0]])
                mtx.insert(0, mtx.pop(d[0]))
                del mtx[1]
                way_now.clear()
                # print(coords)

            distance = get_list_distance(mtx)
            distance = distance[0]
            shortest_way += distance
            shortest_way_coords2.append(mtx[-1])
            # shortest_way_coords = shortest_way_coords[:]

            for i in shortest_way_coords2:
                result.append(i)
            print(result)

            self.dialog = MDDialog(title='Системное оповещение',
                                   text=f'Самый короткий путь: {shortest_way}, маршрут: {result} \n'
                                        f'Данные отправились по Bluetooth микроконтроллеру', size_hint=(0.8, 0),
                                   buttons=[MDFlatButton(text='Ok', on_release=self.close_dialog)]
                                   )
            self.dialog.open()
            # self.label.text = f'Самый короткий путь: {shortest_way}, маршрут: {shortest_way_coords}'
            if len(coords_view) > 12:
                self.label.text = ', '.join(coords_view[:12]) + '...'
                self.x.text = ''
                self.y.text = ''
            else:
                self.label.text = ', '.join(coords_view)
                self.x.text = ''
                self.y.text = ''

            for i in range(len(result)):
                if len(result) > i + 1:
                    plt.plot((result[i][0], result[i + 1][0]),
                             (result[i][1], result[i + 1][1]), alpha=0.6)
                else:
                    plt.plot((result[-1][0], result[0][0]),
                             (result[-1][1], result[0][1]), alpha=0.6)
            # Use adjustable='box-forced' to make the plot area square-shaped as well.
            ax.set_aspect('equal', adjustable='datalim')
            ax.set_xbound(3, 4)

            ax.plot()  # Causes an autoscale update.
            plt.show()

            # coords_view.clear()
            # coords.clear()

            # s = serial.Serial("COM4", 9600)
            # result.append([0, 0])
            # for i in range(len(result)):
            #     if i != 0:
            #         s.write(bytes(result[i]))

        elif METOD[0] == 1:
            if [0, 0] in COORDS:
                COORDS.remove([0, 0])
                # coords_view.remove('(0;0)')
            print('полный перебор')
            print(coords_view)
            fig, ax = plt.subplots()

            route = 0
            list_points = []
            town = 0
            dict_coords = {}
            number_towns_list = []
            shortest_path = 100000
            mtx = []
            vip = []
            coords2 = []

            for i in COORDS:
                # a = f'{random.randint(0, 100)} {random.randint(0, 100)}'
                list_point = i
                coords2.append(list_point[:2])
                if len(list_point) == 3:
                    vip.append(list_point[:2])
                else:
                    mtx.append(list_point)

            if len(vip) != 0:
                vip.insert(0, [0, 0])
            # coords2.insert(0, (0, 0))

            t1 = time.time()
            coords2.insert(0, [0, 0])
            for i in coords2:
                if i not in vip:
                    dict_coords[town] = (i[0], i[1])
                    number_towns_list.append(town)
                    if i[0] == 0 and i[1] == 0:
                        ax.add_patch(plt.Circle((i[0], i[1]), 0.3, facecolor='#FF0000', alpha=1))
                    else:
                        ax.add_patch(plt.Circle((i[0], i[1]), 0.3, facecolor='#9ebcda', alpha=1))

                    # plt.text(i[0] - 0.12, i[1] - 0.12, f'{town}')
                    town += 1
                else:
                    dict_coords[town] = (i[0], i[1])
                    number_towns_list.append(town)
                    if i[0] == 0 and i[1] == 0:
                        ax.add_patch(plt.Circle((i[0], i[1]), 0.4, facecolor='#FF0000', alpha=1))
                    else:
                        ax.add_patch(plt.Circle((i[0], i[1]), 0.4, facecolor='#FF8C00', alpha=1))

                    # plt.text(i[0] - 0.12, i[1] - 0.12, f'{town}')
                    town += 1
            # del coords[0]

            for i in itertools.permutations(number_towns_list):
                for j in i:
                    if list(dict_coords[int(j)]) not in vip:
                        list_points.append(dict_coords[int(j)])
                if len(vip) > 0:
                    for i in vip:
                        list_points.insert(0, (i[0], i[1]))
                else:
                    list_points.insert(0, (0, 0))
                # print(list_points)
                distance = sum(get_list_distance(list_points))
                print(get_list_distance(list_points)[:-1])
                if distance < shortest_path:
                    shortest_path = distance
                    route = copy(list_points)
                list_points.clear()

            t2 = time.time()

            b = route[route[1:].index((0, 0)) + 1:]

            del route[route[1:].index((0, 0)) + 1:]
            route.reverse()
            b.reverse()
            for i in b:
                route.append(i)

            route.insert(0, route.pop())
            print(f'Самый короткий путь: {shortest_path}, маршрут: {route}')
            print(f'Потраченное время: {t2 - t1}')

            self.dialog = MDDialog(title='Системное оповещение',
                                   text=f'Самый короткий путь: {shortest_path}, маршрут: {route} \n'
                                        f'Данные отправились по Bluetooth микроконтроллеру', size_hint=(0.8, 0),
                                   buttons=[MDFlatButton(text='Ok', on_release=self.close_dialog)]
                                   )
            self.dialog.open()
            # self.label.text = f'Самый короткий путь: {shortest_way}, маршрут: {shortest_way_coords}'
            if len(coords_view) > 12:
                self.label.text = ', '.join(coords_view[:12]) + '...'
                self.x.text = ''
                self.y.text = ''
            else:
                self.label.text = ', '.join(coords_view)
                self.x.text = ''
                self.y.text = ''

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

            # coords_view.clear()
            # coords.clear()

            # s = serial.Serial("COM4", 9600)
            # route.append([0, 0])
            # for i in range(len(route)):
            #     if i != 0:
            #         s.write(bytes(route[i]))

        elif METOD[0] == 3:
            def Min(lst, myindex):
                return min(x for idx, x in enumerate(lst) if idx != myindex)

            # функция удаления нужной строки и столбцах
            def Delete(matrix, index1, index2):
                del matrix[index1]
                for i in matrix:
                    del i[index2]
                return matrix

            H = 0
            n = len(COORDS)
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

            for i in COORDS:
                # a = f'{random.randint(0, 100)} {random.randint(0, 100)}'
                # list_point = list(map(int, input().split(' ')))
                if len(i) == 3:
                    vip.append(i[:2])
                else:
                    mtx.append(i)

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
                # print(matrix_vip)
                # print('\n'.join([' '.join([str(cell) for cell in row]) for row in matrix_vip]))
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
                # print("----------------------------------")
                result_sort = list(dict.fromkeys(result))
                result_sort.reverse()

                # print(result)
                # print(result_sort)
                # print()

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
                    # print(PathLenght)
                    # print(coords2)
                    # print("----------------------------------")

                else:
                    dm = np.array(StartMatrix)
                    result, distance = solve_tsp_local_search(dm)
                    # print(result, distance)

                    for i in result:
                        coords2.append(vip[i])
                        if vip[i] != [0, 0]:
                            last_coords.append(vip[i])
                        else:
                            last_coords.insert(0, vip[i])

                if [0, 0] in coords2:
                    coords2.remove([0, 0])
                    coords2.insert(0, [0, 0])

                # print(coords2)
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
                        ax.add_patch(
                            plt.Circle((i[0], i[1]), (0.75 / (n + (n / 0.55))) * n, facecolor='#FF0000', alpha=1))
                        # plt.text(x - 0.12, y - 0.12, f'0')
                    else:
                        ax.add_patch(
                            plt.Circle((i[0], i[1]), (0.75 / (n + (n / 0.55))) * n, facecolor='#9ebcda', alpha=1))
                        # plt.text(x - 0.12, y - 0.12, f'{town}')
                    town += 1

            matrix = m.values.tolist()

            for i in range(len(matrix)):
                matrix[i][i] = float('inf')
                for g in range(len(matrix[i])):
                    matrix[i][g] = round(matrix[i][g], 3)
            # print(matrix)
            # print('\n'.join([' '.join([str(cell) for cell in row]) for row in matrix]))
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
            # print("----------------------------------")
            result_sort = list(dict.fromkeys(result))
            result_sort.reverse()

            # print(result)
            # print(result_sort)
            # print()

            if len(result_sort) == len(mtx):

                # print(result_sort)
                # print()

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
                # print(PathLenght)

                # print("----------------------------------")

            else:
                dm = np.array(StartMatrix)
                result, distance = solve_tsp_local_search(dm)
                # print(result, distance)

                for i in result:
                    coords2.append(mtx[i])
                    last_coords.append(mtx[i])
                    # else:
                    #     last_coords.insert(0, mtx[i])

            # print('*******************************')
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

            # print(last_coords2)
            # print(sum(get_list_distance(last_coords2)))

            self.dialog = MDDialog(title='Системное оповещение',
                                   text=f'Самый короткий путь: {sum(get_list_distance(last_coords2))}, маршрут: {last_coords2} \n'
                                        f'Данные отправились по Bluetooth микроконтроллеру', size_hint=(0.8, 0),
                                   buttons=[MDFlatButton(text='Ok', on_release=self.close_dialog)]
                                   )
            self.dialog.open()
            # self.label.text = f'Самый короткий путь: {shortest_way}, маршрут: {shortest_way_coords}'
            if len(coords_view) > 12:
                self.label.text = ', '.join(coords_view[:12]) + '...'
                self.x.text = ''
                self.y.text = ''
            else:
                self.label.text = ', '.join(coords_view)
                self.x.text = ''
                self.y.text = ''

            for i in range(len(coords2)):
                if len(coords2) > i + 1 and coords2[i + 1] == [0, 0]:
                    plt.plot((coords2[i][0], coords2[-1][0]), (coords2[i][1], coords2[-1][1]), alpha=0.2)

                elif len(coords2) > i + 1:
                    plt.plot((coords2[i][0], coords2[i + 1][0]), (coords2[i][1], coords2[i + 1][1]), alpha=0.2)

                elif len(vip) == 0:
                    plt.plot((coords2[-1][0], coords2[0][0]), (coords2[-1][1], coords2[0][1]), alpha=0.2)

            ax.set_aspect('equal', adjustable='datalim')
            ax.set_xbound(3, 4)

            ax.plot()  # Causes an autoscale update.
            plt.show()

            # s = serial.Serial("COM4", 9600)
            # last_coords2.append([0, 0])
            # for i in range(len(last_coords2)):
            #     if i != 0:
            #         s.write(bytes(last_coords2[i]))

        elif METOD[0] == 5:
            n = len(COORDS)
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

            for i in COORDS:
                # a = f'{random.randint(0, 100)} {random.randint(0, 100)}'
                # list_point = list(map(int, input().split(' ')))
                # coords2.append(list_point[:2])
                if len(i) == 3:
                    vip.append(i[:2])
                else:
                    mtx.append(i)

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
                        plt.plot((last_coords[i][0], last_coords[i + 1][0]), (last_coords[i][1], last_coords[i + 1][1]),
                                 alpha=0.6)
                    else:
                        plt.plot((last_coords[-1][0], last_coords[0][0]), (last_coords[-1][1], last_coords[0][1]),
                                 alpha=0.6)

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
                        plt.plot((last_coords[i][0], last_coords[i + 1][0]), (last_coords[i][1], last_coords[i + 1][1]),
                                 alpha=0.6)
                # print(last_coords2)

                for i in range(len(last_coords2)):
                    if len(last_coords2) > i + 1:
                        plt.plot((last_coords2[i][0], last_coords2[i + 1][0]),
                                 (last_coords2[i][1], last_coords2[i + 1][1]), alpha=0.2)
                    # else:
                    #     plt.plot((last_coords2[-1][0], last_coords2[0][0]), (last_coords2[-1][1], last_coords2[0][1]), alpha=0.6)

            last_coords3 = []

            for i in last_coords:
                if i not in last_coords3:
                    last_coords3.append(i)

            for i in last_coords2:
                if i not in last_coords3:
                    last_coords3.append(i)

            # print(last_coords3, sum(get_list_distance(last_coords3)))

            self.dialog = MDDialog(title='Системное оповещение',
                                   text=f'Самый короткий путь: {sum(get_list_distance(last_coords3))}, маршрут: {last_coords3} \n'
                                        f'Данные отправились по Bluetooth микроконтроллеру', size_hint=(0.8, 0),
                                   buttons=[MDFlatButton(text='Ok', on_release=self.close_dialog)]
                                   )
            self.dialog.open()
            # self.label.text = f'Самый короткий путь: {shortest_way}, маршрут: {shortest_way_coords}'
            if len(coords_view) > 12:
                self.label.text = ', '.join(coords_view[:12]) + '...'
                self.x.text = ''
                self.y.text = ''
            else:
                self.label.text = ', '.join(coords_view)
                self.x.text = ''
                self.y.text = ''

            # Use adjustable='box-forced' to make the plot area square-shaped as well.
            ax.set_aspect('equal', adjustable='datalim')
            ax.set_xbound(3, 4)

            ax.plot()  # Causes an autoscale update.
            plt.show()

            # s = serial.Serial("COM4", 9600)
            # last_coords3.append([0, 0])
            # for i in range(len(last_coords3)):
            #     if i != 0:
            #         s.write(bytes(last_coords3[i]))

        elif METOD[0] == 6:
            n = len(COORDS)
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
            PERCENTAGE_OF_MUTATIONS = 50
            NUMBER_OF_GENERATIONS = 170000
            POPULATIONS = n * 9
            CHILDREN = 2
            stop = [0]

            for i in COORDS:
                # a = f'{random.randint(0, 100)} {random.randint(0, 100)}'
                # list_point = list(map(int, input().split(' ')))
                # coords2.append(list_point[:2])
                if len(i) == 3:
                    vip.append(i[:2])
                else:
                    mtx.append(i)

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

                    # print(list(dict_populations.values())[0], ii)
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
                        plt.plot((last_coords[i][0], last_coords[i + 1][0]), (last_coords[i][1], last_coords[i + 1][1]),
                                 alpha=0.6)
                    else:
                        plt.plot((last_coords[-1][0], last_coords[0][0]), (last_coords[-1][1], last_coords[0][1]),
                                 alpha=0.6)

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
                        plt.plot((last_coords[i][0], last_coords[i + 1][0]), (last_coords[i][1], last_coords[i + 1][1]),
                                 alpha=0.6)
                # print(last_coords2)

                for i in range(len(last_coords2)):
                    if len(last_coords2) > i + 1:
                        plt.plot((last_coords2[i][0], last_coords2[i + 1][0]),
                                 (last_coords2[i][1], last_coords2[i + 1][1]), alpha=0.2)
                    # else:
                    #     plt.plot((last_coords2[-1][0], last_coords2[0][0]), (last_coords2[-1][1], last_coords2[0][1]), alpha=0.6)

            last_coords3 = []

            for i in last_coords:
                if i not in last_coords3:
                    last_coords3.append(i)

            for i in last_coords2:
                if i not in last_coords3:
                    last_coords3.append(i)

            self.dialog = MDDialog(title='Системное оповещение',
                                   text=f'Самый короткий путь: {sum(get_list_distance(last_coords3))}, маршрут: {last_coords3} \n'
                                        f'Данные отправились по Bluetooth микроконтроллеру', size_hint=(0.8, 0),
                                   buttons=[MDFlatButton(text='Ok', on_release=self.close_dialog)]
                                   )
            self.dialog.open()
            if len(coords_view) > 12:
                self.label.text = ', '.join(coords_view[:12]) + '...'
                self.x.text = ''
                self.y.text = ''
            else:
                self.label.text = ', '.join(coords_view)
                self.x.text = ''
                self.y.text = ''

            # Use adjustable='box-forced' to make the plot area square-shaped as well.
            ax.set_aspect('equal', adjustable='datalim')
            ax.set_xbound(3, 4)

            ax.plot()  # Causes an autoscale update.
            plt.show()

            # s = serial.Serial("COM4", 9600)
            # last_coords3.append([0, 0])
            # for i in range(len(last_coords3)):
            #     if i != 0:
            #         s.write(bytes(last_coords3[i]))

        else:
            METOD[0] = 3
            self.redf(0)

            # self.dialog = MDDialog(title='Выберите алгоритм решения!',
            #                        size_hint=(0.4, 0),
            #                        buttons=[MDFlatButton(text='Закрыть', on_release=self.close_dialog)]
            #                        )
            # self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def check(self, checkbox, active):
        if active:
            METOD[0] = 1

    def check1(self, checkbox, active):
        if active:
            METOD[0] = 2

    def check2(self, checkbox, active):
        if active:
            METOD[0] = 3

    def check3(self, checkbox, active):
        if active:
            METOD[0] = 4
        else:
            METOD[0] = -1

    def check4(self, checkbox, active):
        if active:
            METOD[0] = 5

    def check5(self, checkbox, active):
        if active:
            METOD[0] = 6


if __name__ == "__main__":
    Demo().run()
