from exception import InvalidPasswordException, InvalidUserNameException, PasswordToShortException, \
    UserNameAlreadyExistsException
from model import User


class Authenticator:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            raise UserNameAlreadyExistsException(username)
        elif len(password) < 6:
            raise PasswordToShortException(username)
        self.users[username] = User(username, password)

    def login(self, username, password):
        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUserNameException(username)

        if not user.check_password(password):
            raise InvalidPasswordException(username)

        user.is_logged_in = True
        return True

    def is_logged_in(self, username):
        if username in self.users:
            return self.users[username].is_logged_in
        return False
