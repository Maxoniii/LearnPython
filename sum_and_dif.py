def sum_of_digits(n):
    return sum(map(int, str(n)))

def count_digits(n):
    return len(str(n))

number = int(input())

sum_digits = sum_of_digits(number)
count = count_digits(number)

print(f"Сумма чисел: {sum_digits}")
print(f"Количество цифр в числе: {count}")
print(f"Разность суммы и количества цифр: {sum_digits - count}")
