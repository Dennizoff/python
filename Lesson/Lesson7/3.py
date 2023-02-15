class person():
    def __init__(self, name, age, cash = 0):
        self.name = name
        self.age = age
        self.cash = cash
    def zp(self, salary):
        self.cash+=salary

user1 = person("alex",21)

print(user1.cash)

user1.zp(1000)

print(user1.cash)
