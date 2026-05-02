count = int(input("Количество контейнеров: "))

containers = []

for i in range(1, count + 1):
    while True:
        weight = int(input(f"Введите вес контейнера {i}: "))
        if 0 <= weight <= 200:
            break
        print("Вес должен быть не более 200!")
    containers.append(weight)

for i in range(1, len(containers)):
    if containers[i] > containers[i-1]:
        print("Последовательность не является невозрастающей!")

while True:
    new_weight = int(input("\nВведите вес нового контейнера: "))
    if 0 <= new_weight <= 200:
        break
    print("Вес должен быть не более 200!")

position = 1
for weight in containers:
    if new_weight <= weight:
        position += 1
    else:
        break


print(f"\nНомер, который получит новый контейнер: {position}")
