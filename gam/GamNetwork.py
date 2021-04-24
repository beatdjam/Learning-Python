from gam.GoogleAdManagerClient import GoogleAdManagerClient


class GamNetwork:

    def __init__(self):
        self.__service = GoogleAdManagerClient().GetService('NetworkService')

    def get_all_networks(self):
        return self.__service.getAllNetworks()
