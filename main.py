products = []

def menu():
    print("1. Add Products")
    print("2. Show Products")
    print("3. Update Stocks")
    print("4. Delete Products")
    print("5. Search Products")
    print("6. Low Stock Status")

def add_product(details):
    products.append(details)
    print("Add product successfully!")

def view_inventory():
    for index, product in enumerate(products, start=1):
        print(f"{index}. {product["name"]}, price : {product["price"]}, stock : {product["stock"]}.")

def update_stock(product_choice, product_new_value):
    for index, product in enumerate(products, start=1):
        if product_choice == index:
            product["stock"] = product_new_value

def search_products(search_product):
    found = False
    for index, product in enumerate(products, start=1):

        product["name"].lower()

        if search_product.lower() in product["name"]:
            print(f"{index}. {product["name"]}, price : {product["price"]}, stock : {product["stock"]}.")
            found = True
    if not found:
        print("No matching name in products")

def low_stock():
    low_stock = False
    for index, product in enumerate(products, start=1):
        if product["stock"] <= 5:
            print(f"{index}. {product["name"]}, price : {product["price"]}, stock : {product["stock"]}.")
            low_stock = True

    if not low_stock:
        print("No low stock products")
        
            
while True:
    menu()
    try:
        user_input = int(input("Chouse Action: "))
    except ValueError:
        print("Invalid input!")
        continue

    if user_input == 1:

        product_name = input("Enter Product Name: ")
        if product_name.strip() == "":
            print("You don't enter a product name!")
            continue

        product_price = input("Enter Product Price: ")
        if product_price.strip() == "":
            print("You don't enter price")
            continue

        try:
            product_price = int(product_price)
        except ValueError:
            print("Invalid input! Numbers only.")
            continue

        product_stock = input("Enter Stock: ")
        if product_stock == "":
            print("You don't enter stock")
            continue

        try:
            product_stock = int(product_stock)
        except ValueError:
            print("Invalid input! Numbers only.")
            continue

        product_details = {
            "name" : product_name,
            "price" : product_price,
            "stock" : product_stock
            }
        add_product(product_details)

    elif user_input == 2:
        if len(products) == 0:
            print("Empty products")
        else:
            view_inventory()

    elif user_input == 3:
        view_inventory()
        product_choice = input("Choose a number to update stock: ")
        if product_choice.strip() == "":
            print("You didn't enter a stock number")
            continue
        
        try:
            product_choice = int(product_choice)
        except ValueError:
            print("Invalid input! Numbers only.")
            continue

        product_new_value = input("Updated stock value: ")
        if product_new_value.strip() == "":
            print("You didn't enter a new stock value")
            continue

        try: 
            product_new_value = int(product_new_value)
        except ValueError:
            print("Invalid input! Numbers only.")
            continue

        update_stock(product_choice, product_new_value)

    elif user_input == 4:
        view_inventory()

        delete_product = input("Enter product to remove: ")
        if delete_product.strip() == "":
            print("You didn't enter a product number!")
            continue

        try:
            delete_product = int(delete_product)
        except ValueError:
            print("Invalid input! Numbers only.")
            continue

        if len(products) >= delete_product -1 and delete_product -1 >= 0:
            products.pop(delete_product - 1)
    
    elif user_input == 5:
        search_product = input("Enter a product name: ")

        search_products(search_product)

    elif user_input == 6:
        low_stock()

    elif user_input == 9:
        break