m = input()
if m.find("купити") == -1 or m.find('продати') == -1 or m.find("реклама") == -1:
    print("not a spam")
else:
    print("spam")
