def palindrome(lst):
    return lst == lst[::-1]

n = int(input("Кол-во чисел: "))
numbers = []

for i in range(n):
    num = int(input(f"Число: "))
    numbers.append(num)

print(f"\nПоследовательность: {numbers}")

for i in range(n):
    if palindrome(numbers[i:]):
        add = numbers[:i][::-1]
        break

print(f"Нужно приписать чисел: {len(add)}")
print(f"Сами числа: {add}")
