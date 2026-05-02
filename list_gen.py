n = int(input("Введите число: "))

odd_numbers = []
for num in range(1, n + 1):
    if num % 2 != 0:
        odd_numbers.append(num)

print(f"Список из нечётных чисел от одного до N: {odd_numbers}")
