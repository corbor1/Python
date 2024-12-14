my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
count = 0
total_my_list = []
while len(my_list) > count:
    if my_list[count] >= 0:
        total_my_list.append(my_list[count])
        count +=1
    else:
        break
print (total_my_list)