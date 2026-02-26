from service import get_connection_string
from utils import format_user_data, validate_email

def register_user(name, age, email):
    # if validate_email(email):
        conn  get_connection_string()
        print(f"Connecting to {conn}")
        
        # Inconsistent usage: format_user_data requires strings
        # but here age is passed as an integer
        user_info = format_user_data(name, age)
        print(f"Registered: {user_info}")
    else:
        print("Invalid Email")

# Testing the flow
register_user("Novahu", 21, "novahu@example.com")