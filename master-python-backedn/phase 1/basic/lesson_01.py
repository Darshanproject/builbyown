# Exercise 1
# name
# age
# email
# is_verified
name = "Gada Darshan"
age = 26
email = "gada.darshan@example.com"
is_verified = True

print("Name:", name)
print("Age:", age)
print("Email:", email)
print("Is Verified:", is_verified)
# *************************************Exercise 2********************************
age = 13
if age >= 13:
    print("You are child")
elif age > 13 and age < 17:
    print("You are teenager")
elif age > 18:
    print("You are adult")
else:
    print("Something went wrong")
# ***************************************Exercise 3********************************
email = "gadadarshan926@gmail.com"
password = "Gada@1234"
if email == "gadadarshan926@gmail.com" and password == "Gada@1234":
    print("Login successful")
else:
    print("Invalid email or password")
# ***************************************Exercise 4********************************
users = [
    "Darshan",
    "Rahul",
    "Amit",
    "Raj"
]
for user in users:
    print("User:", user)
# *******************************************Challenge 1 *****************************************
username = "Gada926"
password = "Gada@1234"
is_verified = True
if username == "Gada926" and password == "Gada@1234" and is_verified:
    print("Login successful")
elif username == "Gada926" and password == "Gada@1234" and not is_verified:
    print("account must be verified")
elif username == "Gada926" and password != "Gada@1234":
    print("password must be correct")