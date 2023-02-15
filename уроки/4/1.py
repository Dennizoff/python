products = ['Апельсин', 'Банан',"молоко" ,"сир"]
while True:
    command = input("введіть команду: " )
    if command == "exit":
        break
    elif command == "all":
    
        print(products)
    elif command == "add":
        products.append(input("введіть новий продукт: "))
    elif command == "remove":
        product = input("який продукт видалити?:")
        if product in products:
            products.remove(product)
            print(product," видалено")
        else:
            print(product, "немає в списку")
    elif command == "clear":
        products.clear()
        print("список очищено!")
    
    
    else:
        print("невірна команда")
    
