# ******************************************Exercise 1******************************************
def multiply(a: int, b: int) -> int:
    return a * b

print(multiply(4, 6))  # Output: 24
# ******************************************Exercise 2******************************************
def get_username(user_id: int) -> str | None:
    if user_id == 1:
        return "Darshan"
    elif user_id == 2:
        return "Bob"
    else:
        return None

print(get_username(1))  # Output: Darshan
print(get_username(3))  # Output: None
# ******************************************Exercise 3******************************************
def greet(name: str = "Guest") -> str:
    return f"Hello, {name}!"

print(greet())  # Output: Hello, Guest!
print(greet("Alice"))  # Output: Hello, Alice!
# ******************************************Exercise 4******************************************
def calculate_sum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(calculate_sum(10, 20))
print(calculate_sum(10, 20, 30))
print(calculate_sum(1, 2, 3, 4, 5))
# ******************************************Exercise 5******************************************
def create_user(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

create_user(
    name="Darshan",
    email="darshan@example.com",
    age=26,
    is_verified=True
)
# ******************************************Exercise 6******************************************
def create_product(
    name: str,
    price: float,
    quantity: int,
    category: str = "General"
) -> dict:
    return {
        "name": name,
        "price": price,
        "quantity": quantity,
        "category": category
    }


print(create_product("Laptop", 60000, 5, "Electronics"))