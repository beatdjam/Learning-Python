from googleads import AdManagerClient


class GamNetwork:

    def __init__(self, client: AdManagerClient):
        self.__service = client.GetService('NetworkService')

    def get_all_networks(self):
        networks = self.__service.getAllNetworks()
        for network in networks:
            print('Network with network code "%s" and display name "%s" was found.'
                  % (network['networkCode'], network['displayName']))
