# ---------Первое Задание-----------

my_dict = {"andrew" : 1994, "maria" : 2000}
print (my_dict) #--вывод словаря
print (my_dict["andrew"]) #--Вывод для ячейки andrew(Которая сущетвует). Если она отсутствует будет ошибка
print (my_dict.get("URBAN"))#---Просмотр ячейки
my_dict.update({"student" : 2002,
                "teacher" : 1987})#Добавление в словарь
print (my_dict)
del my_dict['maria'] #--Удалиение из ячейки
print (my_dict)
print ("******Второе задание*****")

#*********Второе задание*******

my_set = {1, 2, 3, 4, 4, 3, 2,"text", True, False}
print(my_set)
my_set.add(55)
my_set.add(66)
print(my_set)