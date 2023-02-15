
def mein():
    nums = [1,-4,7,12]
    onlyPlus = []
    for num in nums:
     onlyPlus.append(plus(num))
    print(sum(onlyPlus))



def plus(num):
    if num >= 0:
        return num
    else:
        return 0
    

mein()