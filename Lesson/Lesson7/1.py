# summ = 0
# for i in range(1, 11):
#     summ+=i

# print(summ)

def summ(num, sum):
    if num == 0:
        return sum
    print(num)
    return summ(num-1, sum+num-1)

print(summ(10, 0))

# rec(1)->rex(2)->rex(3)
# def rec(x):
#     if x<4:
#         print(x)
#         rec(x+1)
#         print(x)

# rec(1)
