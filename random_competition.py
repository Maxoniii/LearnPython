import random

t1 = [round(random.uniform(5, 10), 2) for _ in range(20)]
t2 = [round(random.uniform(5, 10), 2) for _ in range(20)]

win = [max(t1[i], t2[i]) for i in range(20)]

print(f"Первая команда: {t1}")
print(f"Вторая команда: {t2}")
print(f"Победители тура: {win}")
