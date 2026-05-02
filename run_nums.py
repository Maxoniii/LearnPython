f = int(input("Сдвиг: "))
nast = [1, 2, 3, 4, 5]

f = f % len(nast)
sdvinyt = nast[-f:] + nast[:-f]

print(f"Сдвинутый список: {sdvinyt}")
