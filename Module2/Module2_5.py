import random


def get_matrix(n, m, start_random, stop_random):
    matrix = []
    value = []
    for i in range(n):
        matrix.append(random.randint(start_random, stop_random))
    for j in range(m):
        value.append(matrix)
        print(value)


one = int(input("Введите кол-во ячеек в [ ]: "))
two = int(input("Введите кол-во столбцов: "))
start_random = int(input("Введите начало диапозона заполнения ячейки: "))
stop_random = int(input("Введите конец диапозона заполнения ячейки: "))
get_matrix(one, two,start_random, stop_random)
