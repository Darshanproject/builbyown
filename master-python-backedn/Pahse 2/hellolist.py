user = ["Darshan", "Rahul", "Amit", "Raj"]
# user[1] = "Gada"
# user.append("Gada")
user.insert(1, "Gada")
print(user)
print(user[-4])
user.pop(1)
# user.remove("Amit")
print(user)
print(len(user))
# for i in user:
#     print("User:", i)
# for index,user in enumerate(user):
#     print(f"User {index+1}: {user}")

print("User:", user[0:2])