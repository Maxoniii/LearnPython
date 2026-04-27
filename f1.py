def bread(func):
    def wrapper():
        return "Bread\n" + func() + "\nBread"
    return wrapper
def salad(func):
    def wrapper():
        return "Salad\n"+ func()
    return wrapper
def saus(func):
    def wrapper():
        return "Saus\n"+func()
    return wrapper
@bread
@salad
@saus
def sasauge():
     return "Sasauge"

print(sasauge())
