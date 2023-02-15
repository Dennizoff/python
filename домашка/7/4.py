def mein():
    list = [1, 2, 2, 7, 9, 8]
    print(step(list))




def step(list):
    summ = 0
    for num in list:
        summ = summ + num ** 2 
    return summ

        






mein()



