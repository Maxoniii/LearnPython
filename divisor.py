def find_min_divisor(n):
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return divisor
    
    return n

number = int(input("Введите число: "))

if number <= 1:
    print("число должно быть больше 1")
else:
    min_divisor = find_min_divisor(number)
    print(f"Наименьший делитель: {min_divisor}")
