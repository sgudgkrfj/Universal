class InvalidPasswordError(Exception):
    def __init__(self, password):
        self.password = password


class InvalidSumbolInPassword(Exception):
    def __init__(self, password):
        self.password = password


def validate_password(password):
    if len(password) >= 8:
        print("Пароль підходить о параметру довжини")
    else:
        raise InvalidPasswordError(password)


def validate_password2(password):
    if " " in password:
        raise InvalidSumbolInPassword(password)
    else:
        print("В паролі не знайдено забороненого символу пробілу")
try:
    password=input("Введіть пароль: ")
    validate_password(password)
    validate_password2(password)
except InvalidPasswordError as e:
    print(f"не правильний пароль '{e.password}'"
          f",треба мінімум 8 символів")
except InvalidSumbolInPassword as d:
    print(f"Пароль {d.password}"
          f" не приймається через присутність забороненого символу пробіл ' '")


