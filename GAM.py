
from googleads import ad_manager
from googleads import oauth2
import os

# 認証ファイルのpathを取得
script_dir = os.path.dirname(__file__)
KEY_FILE = os.path.join(script_dir, 'credential.json')

# Ad Manager API information.
APPLICATION_NAME = 'sample'


def main(key_file, application_name):
    oauth2_client = oauth2.GoogleServiceAccountClient(
        key_file, oauth2.GetAPIScope('ad_manager'))

    ad_manager_client = ad_manager.AdManagerClient(
        oauth2_client, application_name)

    networks = ad_manager_client.GetService('NetworkService').getAllNetworks()
    for network in networks:
        print('Network with network code "%s" and display name "%s" was found.'
              % (network['networkCode'], network['displayName']))


if __name__ == '__main__':
    main(KEY_FILE, APPLICATION_NAME)
