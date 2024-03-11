def distance(point_1, point_2):
    return ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5


def get_list_distance(list_point):
    return [distance(item, list_point[index])
            for index, item in enumerate(list_point, start=-len(list_point) + 1)]


'''
3
1 0
5 0
7 9

5
4 9
6 2
5 7
6 1
6 9
'''
