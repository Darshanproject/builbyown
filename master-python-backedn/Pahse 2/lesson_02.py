# Print the first language.
# Print the last language.
# Add "Python" to the list.
# Remove one language.
# Print the final list.
# Print the length.

languages = ["Java", "C++", "JavaScript", "Go", "Ruby"]

print(languages[0])  # Print the first language
print(languages[-1])  # Print the last language
languages.append("Python")  # Add "Python" to the list
languages.pop(1)  # Remove one language (C++)
print(languages)  # Print the final list
print(len(languages))  # Print the length
# **********************************Exercise 1 completed*********************************
# id
# name
# email
# age
# is_verified
id = {
    "id": 1,
    "name": "Darshan",
    "email": "darshan@example.com",
    "age": 26,
    "is_verified": True
}
id.update({"age":27})
print(id["name"])
id["phone"] = "123-456-7890"
if "phone" in id:
    print("Phone number exists:", id["phone"])

for key, value in id.items():
    print(f"{key}: {value}")

# ***********************************************Exercise 2 completed***********************************************
user ={
    "id":1,
    "name":"Darshan",
    "address":{
        "street":"123 Main St",
        "city":"Anytown",
        "state":"CA",
        "zip":"12345"
    }
}
print(user)
# ***********************************************Exercise 3 completed***********************************************
# {
#     "id": 1,
#     "title": "...",
#     "completed": False
# }

# Then write code to:
# Print all todo titles.
# Print only completed todos.
# Print only incomplete todos.
# Count how many todos are completed.
# Count how many are incomplete.

todos = {
    "1": {
        "id": 1,
        "title": "Buy groceries",
        "completed": False
    },
    "2": {
        "id": 2,
        "title": "Walk the dog",
        "completed": True
    },
    "3": {
        "id": 3,
        "title": "Read a book",
        "completed": False
    },
    "4": {
        "id": 4,
        "title": "Write a blog post",
        "completed": False
    },
    "5": {
        "id": 5,
        "title": "Exercise",
        "completed": True
    }
}
for todo in todos.values():
    print(todo["title"])  # Print all todo titles

for todo in todos.values():
    if todo["completed"]:
        print(todo["title"])  # Print only completed todos

for todo in todos.values():
    if not todo["completed"]:
        print(todo["title"])  # Print only incomplete todos

completed_count = sum(1 for todo in todos.values() if todo["completed"])
print(f"Number of completed todos: {completed_count}")

incomplete_count = sum(1 for todo in todos.values() if not todo["completed"])
print(f"Number of incomplete todos: {incomplete_count}")
# ***********************************************Exercise 4 completed***********************************************
users = [
    {
        "id": 1,
        "name": "Darshan",
        "is_active": True
    },
    {
        "id": 2,
        "name": "Rahul",
        "is_active": False
    },
    {
        "id": 3,
        "name": "Amit",
        "is_active": True
    }
]

for user in users:
    if user["is_active"]:
        print(f"Active user: {user['name']}")
# ***********************************************Exercise 5 completed***********************************************
# mini project*****************************************************************
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

for product in products:
    print(f"Product:{product['name']}")

for product in products:
    if product["in_stock"]:
        print(f"In stock: {product['name']}")
total_price = 0
for product in products:
    total_price += product["price"]
    

print(f"Total price of all products: {total_price}")
total_instock_price = 0
for product in products:
    if product["in_stock"]:
        total_instock_price += product["price"]
print(f"Total price of in-stock products: {total_instock_price}")

max_price_product = max(products, key=lambda x: x["price"])
print(f"Most expensive product: {max_price_product['name']} - Price: {max_price_product['price']}")

out_of_stock_cpunt = sum(1 for product in products if not product["in_stock"])
print(f"Number of out-of-stock products: {out_of_stock_cpunt}")