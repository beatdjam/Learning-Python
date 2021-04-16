from googleads import ad_manager, AdManagerClient
import os

# 認証ファイルのpathを取得
script_dir = os.path.dirname(__file__)
CONFIG_FILE = os.path.join(script_dir, 'googleads.yaml')


def main():
    ad_manager_client: AdManagerClient = ad_manager.AdManagerClient.LoadFromStorage(CONFIG_FILE)

    get_all_networks(ad_manager_client)
    get_current_user(ad_manager_client)


def get_current_user(ad_manager_client: AdManagerClient):
    user = ad_manager_client.GetService('UserService').getCurrentUser()
    print('User with ID %d, name "%s", email "%s", and role "%s" '
          'is the current user.' % (
              user.id, user.name, user.email, user.roleName))


def get_all_networks(ad_manager_client: AdManagerClient):
    networks = ad_manager_client.GetService('NetworkService').getAllNetworks()
    for network in networks:
        print('Network with network code "%s" and display name "%s" was found.'
              % (network['networkCode'], network['displayName']))


if __name__ == '__main__':
    main()
