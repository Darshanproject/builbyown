def create_user(name, email):
    return {"name": name, "email": email, "verified": False}


def get_user_name(user):
    return user["name"]


def is_user_verified(user):
    return user["verified"]