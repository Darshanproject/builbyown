def authenticate_user(username, password, is_verified):

    if username != "admin" or password != "password123":
        return "Invalid username or password"

    if not is_verified:
        return "Account is not verified"

    return "Login successful"


result = authenticate_user("admin", "password123", True)
