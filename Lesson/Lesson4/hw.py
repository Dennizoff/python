# myStr = input("Input str: ")

# for i in range(10):
#     myStr = myStr.replace(str(i), "")

# myStr = "abasdbdfbbbdafabgfbbbbbdgwefew"

# maxIn = 0
# maxChar = ''
# for char in myStr:
#     if(myStr.count(char) > maxIn):
#         maxIn = myStr.count(char)
#         maxChar = char
    
# print(maxChar, maxIn)


goods = [['Апельсин', 6, 150], ['Лимон', 8, 90], ['Картопля', 123, 445]]
sablon = "|{:^5}|{:<26}|{:>12}|{:>12}|"

print("-"*60)
print(sablon.format("#", "Товар", "кількість", "вартість"))
print("-"*60)
count = 0
value = 0
index = 1
for good in goods:
    print(sablon.format(index, good[0], good[1], good[2]))
    index+=1
    count+=good[1]
    value+=good[2]
    
print("-"*60)
print("|{:<32}|{:>12}|{:>12}|".format("продано всього", count, value))
print("-"*60)

mount = [
    ['січень', 31], 
    ['лютий', 28], 
    ['березень', 31],
    ['квітень', 30],
    ['травень', 31],
    ['червень', 30],
    ['липень', 31],
    ['серпень', 31],
    ['вересень', 30],
    ['жовтень', 31],
    ['листопад', 30],
    ['грудень', 31],
]