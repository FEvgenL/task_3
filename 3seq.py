num_input_1 = input('Введите элементы первого списка через один из символов ",", ";", "/": ')
num_input_2 = input('Введите элементы второго списка через один из символов ",", ";", "/": ')
sep_lst = [',', ';', '/']
for sep in sep_lst:
    if sep in num_input_1:
        sep_char_1 = sep
    if sep in num_input_2:
        sep_char_2 = sep
num_lst_1 = list(num_input_1.split(sep_char_1))
num_lst_2 = list(num_input_2.split(sep_char_2))
for char in num_lst_2:
    intermediate_lst = []
    for i in range(len(num_lst_1)):
        if char != num_lst_1[i]:
            intermediate_lst.append(num_lst_1[i])
    num_lst_1 = intermediate_lst
print(sep_char_1.join(num_lst_1))
