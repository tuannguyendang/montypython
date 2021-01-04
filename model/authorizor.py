from exception import InvalidUserNameException, NotPermittedErrorException, PermissionErrorException, \
    NotLoggedInErrorException


class Authorizor:
    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permissions = {}

    def add_permission(self, perm_name):
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            self.permissions[perm_name] = set()
        else:
            raise PermissionErrorException('Permission Exists')

    def permit_user(self, perm_name, username):
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionErrorException('Permission does not exists')
        else:
            if username not in self.authenticator.users:
                raise InvalidUserNameException(username)
            perm_set.add(username)

    def check_permission(self, perm_name, username):
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInErrorException(username)
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionErrorException('Permission does not exists')
        else:
            if username not in perm_set:
                raise NotPermittedErrorException(username)
            return True
