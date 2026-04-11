products = []

def menu():
    print("1. Add Products")

def add_product(details):
    products.append(details)
    print("Add product successfully!")
    
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
            print("You don't enter a product price!")
            continue

        product_stock = input("Enter Stock: ")
        if product_stock.strip() == "":
            print("You don't enter a stock amount!")
            continue

        product_details = {
            "name" : product_name,
            "price" : product_price,
            "stock" : product_stock
            }
        add_product(product_details)
    
    elif user_input == 9:
        break