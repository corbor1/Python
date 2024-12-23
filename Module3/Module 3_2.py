values_list = [14, "test", False]
values_dict = {"a": 14, "b": 69, "c": 55}
values_list_2 = ["str", False]


def print_params(a=1, b='строка', c=True):
    print(a, b, c)


#print_params(*values_list)
#print_params(**values_dict)
#print_params(values_list_2)
values_list_2 = [54.32, 'Строка' ]

print_params(*values_list_2, 42)


