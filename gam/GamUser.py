from gam.GoogleAdManagerClient import GoogleAdManagerClient


class GamUser:

    def __init__(self):
        self.__service = GoogleAdManagerClient().GetService('UserService')

    def get_current_user(self):
        user = self.__service.getCurrentUser()
        print('User with ID %d, name "%s", email "%s", and role "%s" '
              'is the current user.' % (
                  user.id, user.name, user.email, user.roleName))
