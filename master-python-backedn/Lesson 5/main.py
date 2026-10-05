import calcuator 
from calcuator import add
import user_model

result = calcuator.add(5, 3)
print(f"The sum is: {result}")


user = {
    "name": "Darshan",
    "email": "darshan@example.com",
    "is_verified": True
}

user_name = user_model.get_user_name(user)
print(f"User name is: {user_name}")