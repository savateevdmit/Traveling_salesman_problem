import re
# from docx import Document

with open('C:\\Projects\\Traveling-salesman-problem\\ga.txt') as f:
    file = f.readlines()

k = 0
r = []
# doc = Document()
#
# # добавляем таблицу 3x3
# table = doc.add_table(rows=360, cols=4)
# # применяем стиль для таблицы
# table.style = 'Table Grid'

for i in file:
    data_string = i.replace('\n', '')
    if data_string != '':
        # print(data_string)
        try:
        # Извлечение чисел из строки
            numbers_array = re.findall(r'\d+\.\d+', re.search(r'\[(.*?)\]', data_string).group(1))
            numbers_tuple = re.findall(r'\d+\.\d+', re.search(r'\((.*?)\)', data_string).group(1))
        # print(data_string)

        # Извлечение остальной информации
            ng = int(re.search(r'ng = (\d+)', data_string).group(1))

            pm = int(re.search(r'pm = (\d+)', data_string).group(1))
            ppl = int(re.search(r'ppl = (\d+)', data_string).group(1))
            chl = int(re.search(r'chl = (\d+)', data_string).group(1))


            z = '\n'.join([str(round(float(num), 2)) for num in numbers_array])
            i = ''.join(str([round(float(num), 2) for num in numbers_tuple]))

            r.append(float(str(i)[1:-1]))
        except:
            print(data_string)

        # # заполняем таблицу данными
        # data_str = "Generation = {}\nMutation = {}\nPopulation = {}\nCrossover = {}".format(ng, pm, ppl, chl)
        # print(k)
        # for col in range(4):
        #     # получаем ячейку таблицы
        #     cell = table.cell(k, col)
        #     # записываем в ячейку данные
        #     if col == 0:
        #         cell.text = str(k + 1)
        #     elif col == 1:
        #         cell.text = data_str
        #     elif col == 2:
        #         cell.text = str(z)
        #     elif col == 3:
        #         cell.text = str(i)[1:-1]
        #
        #     doc.save('C:\\Projects\\Traveling-salesman-problem\\ga.docx')
        #
        # k += 1

r.sort(reverse=True)
print(r)
