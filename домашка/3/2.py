Name = str(input("your name: "))
latter = Name[0]
count = 0
for i in Name:
    if i == latter:
        count = count + 1
print(count)
#чому іноді програма враховує символи кореня папки?