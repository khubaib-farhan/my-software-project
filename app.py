def hello_world():
    print("Hello from the main branch, SPM Project!") # Modified this line

# Some other unrelated line that might just be added here in main
# e.g., print("This is a new line on main branch.")

def login_user(username, password):
    if username == "admin" and password == "password123":
        print(f"User {username} logged in successfully!")
        return True
    else:
        print("Invalid credentials.")
        return False

if __name__ == "__main__":
    hello_world()
    # login_user("admin", "password123") # Uncomment to test