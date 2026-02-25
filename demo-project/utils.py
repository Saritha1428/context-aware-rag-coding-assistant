def format_user_data(name, age):
    # Bug: age ni string ki marchakunda concatenate chestunnam
    # Idi AI vethakali
    return "User: " + name + " | Age: " + age 

def validate_email(email):
    return "@" in email