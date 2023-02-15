print("-"*54)

mounts = [
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
days = 0

shablon = "|{:<10}|{:<30}|{:>10}|"
print("|{:<10}|{:<30}|{:>10}|".format("#","mouths","days"))
index = 1
print("-"*54)
for mount in mounts:
    print(shablon.format(index, mount[0],mount[1]))
    index = index + 1
    days = days + mount[1]
print("-"*54)
print("|{:<10}{:>42}|".format ("summ", days))
print("-"*54)

    
