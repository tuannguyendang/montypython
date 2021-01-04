from exception import InvalidPasswordException, InvalidUserNameException, NotLoggedInErrorException, \
    NotPermittedErrorException, PermissionErrorException
from model import Authenticator, Authorizor

authenticator = Authenticator()

authorizor = Authorizor(authenticator)

authenticator.add_user("tuan", "tuan123haha")
authorizor.add_permission("test program")
authorizor.add_permission("change program")
authorizor.permit_user("test program", "tuan")


class AuthMenu:
    def __init__(self):
        self.username = None
        self.menu_map = {
            "login": self.login,
            "test": self.test,
            "change": self.change,
            "quit": self.quit,
        }

    def login(self):
        logged_in = False
        while not logged_in:
            username = input('username: ')
            password = input('password: ')
            try:
                logged_in = authenticator.login(username, password)
            except InvalidUserNameException:
                print('Sorry! that username does not exists')
            except InvalidPasswordException:
                print('Sorry! incorrect password')
            else:
                self.username = username

    def is_permitted(self, permission):
        try:
            authorizor.check_permission(permission, self.username)
        except NotLoggedInErrorException as e:
            print('{} is not logged'.format(e.username))
            return False
        except NotPermittedErrorException as e:
            print('{} can not {}'.format(e.username, permission))
            return False
        except PermissionErrorException as e:
            print(e.username)
            return False
        else:
            return True

    def test(self):
        if self.is_permitted('test program'):
            print('Testing program now ...')

    def change(self):
        if self.is_permitted('change program'):
            print('Change program now ...')

    def quit(self):
        raise SystemExit()

    def menu(self):
        try:
            answer = ''
            while True:
                print("""
                please enter command:
                \tlogin\tLogin
                \ttest\tTest
                \tchange\tChange
                \tquit\tQuit""")
                answer = input('enter command : ').lower()
                try:
                    func = self.menu_map[answer]
                except KeyError:
                    raise print('{} is not valid option'.format(answer))
                else:
                    func()
        finally:
            print('Thank for testing auth')


AuthMenu().menu()
