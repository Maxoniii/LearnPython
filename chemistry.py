elements = {}

class Element:
    def __init__(self, name):
        self.name = name
        elements[name] = self
    
    def __add__(self, other):
        pairs = {
            ("огонь", "вода"): "пар",
            ("огонь", "воздух"): "молния",
            ("огонь", "земля"): "лава",
            ("вода", "воздух"): "туман",
            ("вода", "земля"): "грязь",
            ("воздух", "земля"): "пыль",
        }
        key = tuple(sorted([self.name, other.name]))
        if key in pairs:
            result_name = pairs[key]
            if result_name in elements:
                return elements[result_name]
            else:
                return Element(result_name)
        return None


fire = Element("огонь")
water = Element("вода")
air = Element("воздух")
earth = Element("земля")


while True:
    print("\nДоступно: огонь, вода, воздух, земля")
    e1 = input("Первый элемент: ").strip().lower()
    if e1 == "выход": break
    e2 = input("Второй элемент: ").strip().lower()
    if e2 == "выход": break
    
    if e1 not in elements or e2 not in elements:
        print("Ошибка: такой элемент не найден!")
        continue
    
    result = elements[e1] + elements[e2]
    if result:
        print(f"{e1}+{e2} = {result.name}")
    else:
        print(f"{e1}+{e2}=ничего")
