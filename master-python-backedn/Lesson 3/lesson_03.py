def greet(name):
    print(f"Hello, {name}!")

greet("Darshan")
# ******************************************Exercise 1******************************************
def addNumbers(a, b):
    return a + b

result = addNumbers(10, 5)
print(f"The sum is: {result}")
# ******************************************Exercise 2******************************************
def calcuate_total(price, quantity):
    return price * quantity

calculation = calcuate_total(20, 3)
print(f"The total cost is: {calculation}")

# ******************************************Exercise 3******************************************
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(10))
# ******************************************Exercise 4******************************************
def authenticate_user(username, password, is_verified):

    if username != "admin" or password != "password123":
        return "Invalid username or password"

    if not is_verified:
        return "Account is not verified"

    return "Login successful"


result = authenticate_user("admin", "password123", True)

print(result)
# ******************************************Exercise 5******************************************
def get_total_price(products):
    total_price = 0
    for product in products:
        total_price += product['price'] * int(product['in_stock'])
    return total_price

def get_in_stock_products(products):
    in_stock_products = []
    for product in products:
        if product['in_stock'] == True:
            in_stock_products.append(product)
    return in_stock_products

def get_most_expensive_product(products):
    most_expensive_product = products[0]
    for product in products:
        if product['price'] > most_expensive_product['price']:
            most_expensive_product = product
    return most_expensive_product

def get_out_of_stock_count(products):
    count = 0
    for product in products:
        if product['in_stock'] == False:
            count += 1
    return count
products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 60000,
        "in_stock": True
    },
    {
        "id": 2,
        "name": "Mouse",
        "price": 1000,
        "in_stock": True
    },
    {
        "id": 3,
        "name": "Keyboard",
        "price": 2500,
        "in_stock": False
    },
    {
        "id": 4,
        "name": "Monitor",
        "price": 15000,
        "in_stock": True
    }
]


print(get_total_price(products))
print(get_in_stock_products(products))
print(get_most_expensive_product(products))
print(get_out_of_stock_count(products))