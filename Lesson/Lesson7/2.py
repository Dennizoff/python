class Person():
    def __init__(self, name, age, yearWork, cash):
        self.name = name
        self.age = age
        self.yearWork = yearWork
        self.cash = cash
    def salaryAdd(self, salary):
        self.cash += salary
        print("Зарплата начислена")

class Company():
    salary = 3000

company1 = Company()
user1 = Person("Bill", 20, 5, 5000)

print(user1.cash)

user1.salaryAdd(company1.salary)

print(user1.cash)




