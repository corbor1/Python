numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for num in numbers:
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                not_primes.append(num)
                break
        else:
            primes.append(num)
    else:
        primes.append(num)

print("Простые числа:")
print(primes)

print("Не простые числа:")
print(not_primes)