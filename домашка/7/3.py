def mein():
    string = input("you string: ")
    print(action(string))

def action(string):
    if len(string) <= 2:
        return string
    else:
     s = list(string) # заносим строку string в список s
    del s[0] # видаляєм зі списку s елемент з індексом 0
    del s[-1]
    return "".join(s) # перетворюєм список s в строку, в лапках вказуємо знак який розділятиме елементи списку


mein()