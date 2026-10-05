def add_numbers(a:int ,b:int) -> int:
    return a + b

print(add_numbers(5, 3))  # Output: 8

def greet(name:str) -> str:
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!

def get_number() -> list[int]:
    return [1, 2, 3, 4, 5]

print(get_number())  # Output: [1, 2, 3, 4, 5]

def get_name() -> list[str]:
    return ["Alice", "Bob", "Charlie"]

print(get_name())  # Output: ['Alice', 'Bob', 'Charlie']

def get_user_info() -> dict:
    return {"id": 1, "name": "Alice", "age": 30}

print(get_user_info())  # Output: {'id': 1, 'name': 'Alice', 'age': 30}

def get_phone() -> str | None:
    return None

print(get_phone())  # Output: None

def greet(name: str = "Guest") -> str:
    return f"Hello, {name}!"

print(greet())  # Output: Hello, Guest!
print(greet("Alice"))  # Output: Hello, Alice!

def add_numbers2(a=10,b=5):
    return a + b

print(add_numbers2())  # Output: 15
print(add_numbers2(20, 30))  # Output: 50

def add_numbers(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total

print(add_numbers(10, 20))
print(add_numbers(10, 20, 30))
print(add_numbers(10, 20, 30, 40, 50))

def create_user(**data):
    print(data)

create_user(
    name="Darshan",
    email="darshan@example.com",
    age=26
)

name = "Darshan"

def greet():
    name = "Rahul"
    print(name)

greet()

print(name)

