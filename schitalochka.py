n = int(input("Кол-во человек: "))
k = int(input("Какое число в считалке? "))
print(f"Значит, выбывает каждый {k} человек\n")

people = list(range(1, n + 1))
ind = 0

while len(people) > 1:
    print(f"Текущий круг людей: {people}")
    print(f"Начало счёта с номера {people[ind]}")
    
    ind = (ind + k - 1) % len(people)
    delete = people.pop(ind)
    
    print(f"Выбывает человек под номером {delete}\n")

    if ind == len(people):
        ind = 0
    

print(f"Остался человек под номером {people[0]}")
