import uuid

from googleads import ad_manager, AdManagerClient
import os

# 認証ファイルのpathを取得
from googleads.errors import GoogleAdsServerFault

script_dir = os.path.dirname(__file__)
CONFIG_FILE = os.path.join(script_dir, 'googleads.yaml')


def main():
    ad_manager_client: AdManagerClient = ad_manager.AdManagerClient.LoadFromStorage(CONFIG_FILE)

    get_all_networks(ad_manager_client)
    get_current_user(ad_manager_client)
    get_all_companies(ad_manager_client)
    get_all_orders(ad_manager_client)
    add_advertiser(ad_manager_client)


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


def get_all_companies(ad_manager_client: AdManagerClient):
    company_service = ad_manager_client.GetService('CompanyService')

    # 何も指定せず会社をすべて取得する
    statement = ad_manager.StatementBuilder()

    # 広告主・自社広告主を取得する場合のStatement
    # statement = ad_manager.StatementBuilder()\
    #     .Where('type IN (\'ADVERTISER\' , \'HOUSE_ADVERTISER\')')

    while True:
        response = company_service.getCompaniesByStatement(statement.ToStatement())
        if 'results' in response and len(response['results']):
            for company in response['results']:
                print('Company with ID "%d", name "%s", and type "%s" was found.\n' %
                      (company['id'], company['name'], company['type']))
            statement.offset += statement.limit
        else:
            break

    print('\nNumber of results found: %s' % response['totalResultSetSize'])


# 広告主を追加する
def add_advertiser(ad_manager_client: AdManagerClient):
    try:
        company_service = ad_manager_client.GetService('CompanyService')
        # 追加するサンプル
        companies = [
            {
                'name': 'Advertiser by API',
                'type': 'ADVERTISER'
            }
        ]
        companies = company_service.createCompanies(companies)
        for company in companies:
            print('Company with ID "%d", name "%s", and type "%s" was found.\n' %
                  (company['id'], company['name'], company['type']))
    except GoogleAdsServerFault as e:
        # TODO すでに存在していた場合のエラー処理
        print(e)
        print('already exists.')


# アーカイブされていないオーダーを取得する
def get_all_orders(client: AdManagerClient):
    service = client.GetService('OrderService')
    statement = ad_manager.StatementBuilder().Where('isArchived = FALSE')
    while True:
        response = service.getOrdersByStatement(statement.ToStatement())
        if 'results' in response and len(response['results']):
            for order in response['results']:
                print('Order with ID "%d" and name "%s" was found.\n' % (order['id'],
                                                                         order['name']))
            # 全件読み込むためにlimitにoffsetを足してループ
            statement.offset += statement.limit
        else:
            break


# オーダーを作成する
def add_order(client: AdManagerClient, advertiser_id: int, trafficker_id: int):
    service = client.GetService('OrderService')

    orders = []
    for _ in range(1):
        order = {
            'name': 'Order #%s' % uuid.uuid4(),
            'advertiserId': advertiser_id,
            'traffickerId': trafficker_id
        }
        orders.append(order)

    orders = service.createOrders(orders)
    for order in orders:
        print('Order with id "%s" and name "%s" was created.'
              % (order['id'], order['name']))


if __name__ == '__main__':
    main()
