
# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def hello(self):
#         return "Hi "+self.name
    
# user1 = Person("Bill", 20)

# print(user1.hello())



class animal():
    def __init__(self, name, voice):
        self.name = name
        self.voice = voice
    def say(self):
        return self.name + " говорит: "  + self.voice
animal1 = animal("cow", "myy")
print(animal1.say())