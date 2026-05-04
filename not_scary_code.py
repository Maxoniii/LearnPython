main = [1,5,3]
first = [1,5,1,5]
second = [1,3,1,5,3,3]

main += first
print(f"Количество цифр 5 при первом объединении: {main.count(5)}")

main = [x for x in main if x!=5]
main += second
print(f"Количество цифр 3 при втором объединении: {main.count(3)}")
print(f"Итоговый список: {main}")
