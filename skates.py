skates_cnt = int(input("Кол-во коньков: "))
skates = []
for i in range(1, skates_cnt +1):
    size = int(input(f"Размер {i} пары: "))
    skates.append(size)

people_cnt = int(input("\n Кол-во людей: "))
people = []
for i in range(1,people_cnt +1):
    size = int(input(f"Размер ноги {i} человека: "))
    people.append(size)

skates.sort()
people.sort()

used = [False] *len(skates)
sovpal = 0
for person_size in people:
    for i in range(len(skates)):
        if not used[i] and skates[i]>= person_size:
            used[i] = True
            sovpal+=1
            break
print(f"Наибольшее кол-во людей, которые могут взять ролики: {sovpal}")
