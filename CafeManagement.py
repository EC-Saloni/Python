def orderFood():
    d1 = {
        "Pizza" : 400,
        "Pasta" : 200,
        "Coffee" : 150,
        "SoftDrink" : 100,
        "Burger" : 180
    }
    print("Welcome to our Restaurant.")
    print("MENU \n Pizza: 400 \n Pasta: 200 \n Coffee: 150 \n SoftDrink : 100 \n Burger : 180")
    total = 0
    item1 = input("What do you want to order:")
    if item1 in d1:
        total += d1[item1]
        print(f"Your item {item1} has been added to your order!")
    else:
        print(f"The item {item1} is not available in the restaurant yet!!")
    
    moreOrder = input("Do you want to add more item?(Yes/No)")
    if(moreOrder == "Yes"):
        item2 = input("Want do you want to add:")
        if item2 in d1:
            total += d1[item2]  
        else:
            print(f"Item {item2} is not available!")
    print(f"Total amount of items to pay is {total}")

orderFood()

