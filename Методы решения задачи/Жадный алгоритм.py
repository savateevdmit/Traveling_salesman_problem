import random

from distance_calculation import get_list_distance

coords2 = []
list_points = []
way_now = {}
shortest_way = 0
shortest_way_coords = [[0, 0]]
shortest_way_coords2 = []
mtx = []
vip = []
result = []

for i in range(int(input())):
    # a = f'{random.randint(0, 100)} {random.randint(0, 100)}'
    list_point = list(map(int, input().split(' ')))
    coords2.append(list_point[:2])
    if len(list_point) == 3:
        vip.append(list_point[:2])
    else:
        mtx.append(list_point)

if len(vip) != 0:
    vip.insert(0, [0, 0])
coords2.insert(0, (0, 0))


# vip.insert(0, [9, 9])
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



