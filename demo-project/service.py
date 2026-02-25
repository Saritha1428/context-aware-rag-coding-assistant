# Database configuration details
DB_NAME = "users_db"
DB_HOST = "localhost"
DB_PORT = 5432

def get_connection_string():
    return f"postgresql://{DB_HOST}:{DB_PORT}/{DB_NAME}"