shop = [['каретка', 1200], 
    ['шатун', 1000], 
    ['седло', 300], 
    ['педаль', 100], 
    ['седло', 1500], 
    ['рама', 12000], 
    ['обод', 2000], 
    ['шатун', 200], 
    ['седло', 2700]
]

detail_name = input("Название детали: ")
cnt = 0
total_cnt = 0
for name, price in shop:
    if name == detail_name:
        cnt +=1
        total_cnt += price

if cnt>0:
    print(f"Кол-во деталей: {cnt}")
    print(f"Общая стоимость: {total_cnt}")
else:
    print(f"Деталь '{detail_name}' не найдена в магазе")
