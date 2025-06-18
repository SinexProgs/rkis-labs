class User:
    _login = ''
    _password = ''

    def __init__(self, login, password):
        self._login = login
        self._password = password

    @property
    def login(self):
        return self._login

    @property
    def password(self):
        return self._password

    def __str__(self):
        return f"Login: {self._login}, Password: {self._password}"


users = [User("Oleg", "1234321"),
         User("Penkin", "15263748"),
         User("Stas", "poshel"),
         User("Maksim", "zdes"),
         User("Kirill", "qwerty")]

login = input("Enter your login: ")
password = input("Enter your password: ")
for user in users:
    if user.login == login and user.password == password:
        print(user)