num_items = int(input('Введите количество элементов: '))
num_lst = []
for item in range(num_items):
    item_lst = int(input(f'Введите {item + 1} элемент: '))
    num_lst.append(item_lst)
num_lst.sort()
print(f'Вывод: {num_lst}')