s = 'hello'

# print(str[-1:-4:-1])

# print(s.title().swapcase())
# title()
# lower()
# upper()
# capitalize()
# swapcase()

# print(s.find("llll"))
# print(s.split(","))
# print(s.replace(",", ""))
# print(f" Hi,  {s} , end")
# print("|{:<10}|{:^10}|".format(s, s))

# print(m.find("купити"))

# m = input()
# m = "купити щось"
# if m.find("купити") == -1 and m.find('продати') == -1 and m.find("реклама") == -1:
#     print("not a spam")
# else:
#     print("spam")

# print(m.find("купити"), m.find("купити") == -1)
# print(m.find("продати"), m.find('продати') == -1)
# print(m.find("реклама"), m.find("реклама") == -1)

list = []
for i in range (1 , 10):
    list2 = []
    for j in range (1,10):
        list2.append(i * j)
    list.append(list2)

print("-"*55)
for el in list:
    print("|", end="")
    for i in el:
        print("{:^5}|".format(i), end="")
    print()
    print("-"*55)

