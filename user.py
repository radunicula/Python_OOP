class User:
    def __init__(self, first_name, profile):
        self.first_name = first_name
        self.profile = profile
        self.login_attempts = 0

    def describe_user(self):
        return f"user name:{self.first_name}, user profile:{self.profile}"

    def greet_user(self):
        return f'Hello {self.first_name} you are {self.profile}!'

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        return self.privileges


class Admin(User):
    def __init__(self, first_name, profile):
        super().__init__(first_name, profile)
        self.privileges = Privileges()
