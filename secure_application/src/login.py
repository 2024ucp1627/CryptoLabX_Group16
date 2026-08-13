class Login:
    def __init__(self):
        # Intentionally hardcoded credentials (assignment vulnerability)
        self.username = "admin"
        self.password = "admin123"

    def login(self):
        print("\n===== LOGIN =====")

        username = input("Username: ")
        password = input("Password: ")

        if username == self.username and password == self.password:
            print("\nLogin Successful!\n")
            return True

        print("\nInvalid Username or Password.\n")
        return False

    def logout(self):
        print("\nLogged out successfully.\n")