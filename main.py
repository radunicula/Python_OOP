from user import User, Privileges, Admin

radu = Admin("Radu", "admin")
radu.describe_user()
radu.login_attempts = 4
print(radu.login_attempts)
radu.reset_login_attempts()
print(radu.login_attempts)
radu.increment_login_attempts()
print(radu.login_attempts)

