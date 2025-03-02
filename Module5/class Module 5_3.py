class House:
    def __init__(self, name, number_of_floors):
        self.name = name  # горский
        self.number_of_floors = number_of_floors  # 18

    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей:{self.number_of_floors}'

    def __eq__(self, other):#== ??????????????
        return self.number_of_floors == other

    def __lt__(self, other): #<
        return self.number_of_floors<other

    def __le__(self, other):# <=
        return self.number_of_floors <= other

    def __gt__(self, other):#(>),
        return self.number_of_floors > other

    def __ge__(self, other):#>=
        return self.number_of_floors >= other

    def __ne__(self, other):#!=
        return self.number_of_floors != other

    def __add__(self, other):
        self.number_of_floors += other
        return f'Название: {self.name}, кол-во этажей:{self.number_of_floors}'

    def __radd__(self, other):
        self.number_of_floors += 1
        return self.number_of_floors

    def __iadd__(self, other):
        self.number_of_floors += 1
        return self.number_of_floors

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)#Название: ЖК Эльбрус, кол-во этажей:10
print(h2)#Название: ЖК Акация, кол-во этажей:20
print(h1 == h2) # __eq__ False

h1 = h1 + 10 # __add__ Название: ЖК Эльбрус, кол-во этажей:20

print(h1)
print(h1 == h2)

h1 += 10 # __iadd__

print(h1)

h2 = 10 + h2 # __radd__

print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

