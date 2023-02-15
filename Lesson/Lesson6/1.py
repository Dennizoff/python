# def minus(num):
#     return num if num < 0 else num*-1

# def main():
#     num = int(input("your number: "))
#     print(minus(num))

# main()

# def substr(strs):
#     return strs[::2]

# string = "abscdf"

# print(substr(string))

# {"Bill":[{"height":177}, 77, "Lviv"]}





class profesions():
    profesion = "artist"

class Person(profesions):
    name = "user"
    age = 20
    
    def hello(self):
        return "Hi "+self.name+","+self.profesion
    
    # def age18(self, minage):
    #     if(self.age >=minage):
    #         return "є "+str(minage)
    #     else:
    #         return "немає "+str(minage)

user1 = Person()
user1.name = "Bill"
user1.age = 5
# user2 = Person()

print(user1.hello())


# print(user1.age18(20))
# print(user2.name)

