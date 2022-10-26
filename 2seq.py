num_input = input('Введите элементы списка через один из символов ",", ";", "/": ')
sep_lst = [',', ';', '/']
for sep in sep_lst:
    if sep in num_input:
        sep_char = sep
        break
num_lst = set(num_input.split(sep_char))
print(sep_char.join(num_lst))