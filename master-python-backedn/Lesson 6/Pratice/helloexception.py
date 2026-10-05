# def divide(a: float, b: float) -> float:
#     if b == 0:
#         # raise ValueError("Cannot divide by zero.")
#         try:
#             print("Enter proper numbers")
#         except:
#             print("Cannot divide by zero.")

#     return a / b


# a = int(input("Enter the numerator: "))
# b = int(input("Enter the denominator: "))
# divide(a, b)

# age = input("Enter your age: ")

# try:
#     age = int(age)
#     print(f"Your age is {age}")
# except ValueError:
#     print("Please enter a valid number")


# amount <= 0
# → "Amount must be greater than zero"

# amount > balance
# → "Insufficient balance"

# otherwise
# → return remaining balance

# def withdraw(balance: float, amount: float) -> float:
#     if amount <= 0:
#         raise ValueError("Amount must be greater than zero")
#     elif amount > balance:
#         raise ValueError("Insufficient balance")
#     else:
#         return balance - amount


# print(withdraw(1000, 1500))  # returns 500

# def get_user_email(user: dict) -> str:
#     try:
#         return user["email"]
#     except KeyError:
#         raise ValueError("User does not have an email address")

# user = {"name": "Darshan", "email": "darshan@example.com"}
# user1 = {"name": "Meet"}

# print(get_user_email(user))  # returns "
# print(get_user_email(user1))  # raises ValueError: User does not have an email address

# def create_user(name: str, age: int) -> dict:
#     if not name:
#         raise ValueError("Name cannot be empty")
#     if age < 0:
#         raise ValueError("Age cannot be negative")
#     return {"name": name, "age": age}

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))

# print(create_user(name, age))

# 1. Valid transfer
# 2. Zero amount
# 3. Negative amount
# 4. Amount greater than balance
def transfer_money(
    sender_balance: float,
    amount: float
) -> float:
    if amount <= 0:
        raise ValueError("Amount must be greater than zero")
    elif amount > sender_balance:
        raise ValueError("Insufficient balance")
    else:
        return sender_balance - amount

print(transfer_money(1000, 500))  # returns 500
