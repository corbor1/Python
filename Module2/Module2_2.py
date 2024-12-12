a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

if a == b and a == c:
    print("3")
elif a != b and a != c and b != c:
    print ("0")
else:
    print("2")
