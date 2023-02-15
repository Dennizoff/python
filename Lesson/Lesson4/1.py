currencies = {'USD':40.3, "EUR":42}
# test = {'a': 1, 'b': 2}
currencies['EUR'] = 50
currencies['UAN'] = 10
currencies.pop('EUR')
for key, value in currencies.items():
    print(key, value)

