from user import User


class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        return self.privileges


class Admin(User):
    def __init__(self, first_name, profile):
        super().__init__(first_name, profile)
        self.privileges = Privileges()


radu = Admin(first_name="Radu", profile="admin")
print(radu.privileges.show_privileges())
