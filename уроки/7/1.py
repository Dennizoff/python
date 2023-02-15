def summ(num1, num2):
   sum = num1 + num2
   return sum

def minus(num1, num2):
   min = num1 - num2
   return min

def dilenia(num1,num2):
    return num1/num2

def multi(a, b):
    return a * b

def main():
    string  = input("введіть данні через пробіл: ").split()
    num1 = int(string[0])
    num2 = int(string[2])
    action = string[1]
    if action == "+":
        print(summ(num1, num2))
    elif action == "-":
        print( minus(num1, num2))
    elif action == "/":
        print((dilenia(num1,num2)))
    elif action == "*":
        print(multi(num1,num2))
    else:
        print("невідома команда")
main()

