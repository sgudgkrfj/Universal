class InvalidUrlError(Exception):
    def __init__(self, username):
        self.username = username


def register_user(username):
    if len(username) < 5:
        raise InvalidUrlError(username)
    else:
        print("vas zaregano")

try:
    username = input("Введіть ім'я користувача")
    register_user(username)
except InvalidUrlError as e:
    print(f"Неправильне ім'я користувача {e.username}!"
          f"Треба мінімум 5 символів!")




