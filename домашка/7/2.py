def minus(num):
    return num * -1
    
def plus(num):
    return num

def mein():
    num = int(input("your number: "))
    if num >= 0:
        print(minus(num))
    else:
        print(plus(num))
mein()