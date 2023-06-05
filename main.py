class UserNotFoundError(Exception):
    pass

class UserDatabase:
    def __init__(self):
        self.users = {}

    def add_user(self, username, user):
        self.users[username] = user

    def get_user(self, username):
        if username in self.users:
            return self.users[username]
        else:
            raise UserNotFoundError(f"User '{username}' not found")


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

user_db = UserDatabase()

user1 = User("john", "john@example.com")
user2 = User("jane", "jane@example.com")
user_db.add_user(user1.username, user1)
user_db.add_user(user2.username, user2)


try:
    username = input("Введіть ім'я користувача: ")
    user = user_db.get_user(username)
    print("Знайдений користувач:", user.username, user.email)
except UserNotFoundError:
    print(f"Користувача не знайдено")