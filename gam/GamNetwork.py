from gam.GoogleAdManagerClient import GoogleAdManagerClient


class GamNetwork:

    def __init__(self):
        self.__service = GoogleAdManagerClient().GetService('NetworkService')

    def get_all_networks(self):
        networks = self.__service.getAllNetworks()
        for network in networks:
            print('Network with network code "%s" and display name "%s" was found.'
                  % (network['networkCode'], network['displayName']))
