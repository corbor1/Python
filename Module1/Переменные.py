homework = float(input("Введите количество выполненых ДЗ: "))
all_hour = float(input("Введите количество затраченых часов: "))
Course = "Python"
summ = all_hour / homework
print ("Курс: ",Course,"\nВсего задач:",homework, "\nЗатрачено часов: ",all_hour, "\nСреднее время выполнения" ,summ, "час.")