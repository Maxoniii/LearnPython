text = input("Введите текст: ")

glasn = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
glasn_list = [char for char in text.lower() if char in glasn]

print(f"Список гласных букв: {glasn_list}")
print(f"Длина списка: {len(glasn_list)}")
