from gam.GoogleAdManagerClient import GoogleAdManagerClient


class GamUser:

    def __init__(self):
        self.__service = GoogleAdManagerClient().GetService('UserService')

    def get_current_user(self):
        return self.__service.getCurrentUser()
