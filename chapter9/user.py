class Users:
    """a class to define users information"""

    def __init__(self, first, last, username, password, dob):
        """Inizializtion Users infromation"""
        self.first = first
        self.last = last
        self.username = username
        self.password = password
        self.dob = dob
        self.age = 0
        self.login_attempt = 0

    def get_user_info(self):
        """retrun a dic of object contains user information"""
        user = {
            "full_name": f"{self.first} {self.last}",
            "first_name": self.first,
            "last_name": self.last,
            "user_name": self.username,
            "date_of_birth": self.dob
        }

        return user

    def increment_login_attempts(self, login):
        """a method to increment each time user loged in"""
        if login >= self.login_attempt:
            self.login_attempt = login
        else:
            print("You can't roll back!!!")

    def reset_login_attempts(self):
        """Reset Login attempt to (0)"""
        self.login_attempt = 0

    def greed_user(self):
        print(f"Hello, {self.first} {self.last}")

