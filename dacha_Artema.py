friends = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
best_friends = 6

print(f"Сейчас на вечеринке {len(friends)} человек: {friends}")

while True:
    action = input("Гость пришёл или ушёл? ")
    if action == "Пора спать":
        break

    name = input("Имя гостя: ")
    if action == "пришёл":
        if len(friends) < best_friends:
            friends.append(name)
            print(f"Привет, {name}!")
        else:
            print(f"Прости, {name}, но мест нет.")
    
    elif action == "ушёл":
        if name in friends:
            friends.remove(name)
            print(f"Пока, {name}!")
        else:
            print(f"Гостя {name} нет на вечеринке")
    
    print(f"Сейчас на вечеринке {len(friends)} человек: {friends}")

print("\nВечеринка закончилась, все легли спать.")
