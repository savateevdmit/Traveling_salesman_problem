a = [9298, 6090, 6340, 6566, 8235, 6581, 6136, 7922, 3414, 5160]
b = [4212, 2469, 2726, 2987, 4397, 2938, 2710, 3448, 1960, 2370]

d = []
dd = []

c = [a, b]
for i in range(len(c)):
    for j in range(len(c[i])):
        d.append((c[i][j], i + 1))

d.sort(key=lambda tup: tup[0])
print(d)

count = 1
dd = []
gg = []
sr = 0
x = []

counter = {}

for elem in d:
    counter[elem[0]] = counter.get(elem[0], 0) + 1

doubles = [element for element, u in counter.items() if u > 1]

print(doubles)

for i in d:
    g = list(i)
    g.append(count)
    ii = tuple(g)
    dd.append(ii)
    count += 1
print(dd)

ddd = []
if len(doubles) > 0:
    for h in doubles:
        for i, ltr in enumerate(d):
            if ltr[0] == h:
                x.append(i)
        # x = [i for i, ltr in enumerate(d) if ltr[0] == h]
        print(x)  # [0, 2, 5]
        cc = 0
        for i in x:
            cc += dd[i][2]
        sr = cc / len(x)
        print(sr)

        for i in dd:
            if i[0] == h:
                g = list(i)
                g[-1] = sr
                ii = tuple(g)
                ddd.append(ii)
            elif i in ddd or i[0] in doubles:
                pass
            else:
                ddd.append(i)
        x.clear()
else:
    ddd = dd.copy()
print(ddd)

itog = 0
for i in ddd:
    if len(a) < len(b):
        if i[1] == 1:
            itog += i[2]
    else:
        if i[1] == 2:
            itog += i[2]
print(itog)
# print([122, 212])
# if 122 < itog < 212:
#     print('однородные')
# else:
#     print('неоднородные')
#
# print([129, 195])
# if 129 < itog < 195:
#     print('однородные')
# else:
#     print('неоднородные')
