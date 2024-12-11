immutable_var = (True, 1 , 2 , "text")
print (immutable_var )
#3. Изменение значений переменных:
#Попытайтесь изменить элементы кортежа immutable_var.
#Объясните, почему нельзя изменить значения элементов кортежа.
#>>>>>>>>>>>в Кортеже нельзя изменить данные. только Если в нем не присутсвуют [ ], то в этих скаобках
#мы можем менять данные

mutable_list = [True, "Name", 2]
mutable_list.append("New Text")
mutable_list.extend("test")
print (mutable_list)
mutable_list.remove("Name")
print (mutable_list)
mutable_list [0] = False
print (mutable_list)