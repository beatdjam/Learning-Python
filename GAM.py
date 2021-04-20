from googleads import ad_manager, AdManagerClient
import os

# 認証ファイルのpathを取得
from gam.GamCompany import GamCompany
from gam.GamNetwork import GamNetwork
from gam.GamOrder import GamOrder
from gam.GamUser import GamUser

script_dir = os.path.dirname(__file__)
CONFIG_FILE = os.path.join(script_dir, 'googleads.yaml')


def main():
    ad_manager_client: AdManagerClient = ad_manager.AdManagerClient.LoadFromStorage(CONFIG_FILE)

    GamNetwork(ad_manager_client).get_all_networks()
    GamUser(ad_manager_client).get_current_user()
    company = GamCompany(ad_manager_client)
    company.get_all_companies()
    company.create_advertiser('Advertiser by API')
    order = GamOrder(ad_manager_client)
    order.get_all_orders()


if __name__ == '__main__':
    main()
