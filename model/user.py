import hashlib


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self._encrypt_pw_(password)
        self.is_logged_in = False

    def _encrypt_pw_(self, password):
        hash_string = self.username + password
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        encrypted = self._encrypt_pw_(password)
        return encrypted == self.password
