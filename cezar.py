l = input("Введите сообщение: ")
sdvig = int(input("Введите сдвиг: "))

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

res = ''

for char in l:
    if char in alphabet:
        ind1 = alphabet.find(char)
        ind2 = (ind1 + sdvig) % len(alphabet)
        res += alphabet[ind2]
    else:
        res += char

print(f"Зашифрованное сообщение: {res}")
