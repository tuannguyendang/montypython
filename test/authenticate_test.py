from model import Authenticator, Authorizor

authenticator = Authenticator()

authorizor = Authorizor(authenticator)

authenticator.add_user("tuan", "tuan123haha")
authorizor.add_permission("test program")
authorizor.add_permission("change program")
authorizor.permit_user("test program", "tuan")

print(authenticator.users)
print(authorizor.permissions)
