import uuid

from googleads import ad_manager

from gam.GoogleAdManagerClient import GoogleAdManagerClient


class GamOrder:
    def __init__(self):
        self.__service = GoogleAdManagerClient().GetService('OrderService')

    # アーカイブされていないオーダーを取得する
    def get_all_orders(self):
        statement = ad_manager.StatementBuilder().Where('isArchived = FALSE')
        while True:
            response = self.__service.getOrdersByStatement(statement.ToStatement())
            if 'results' in response and len(response['results']):
                for order in response['results']:
                    print('Order with ID "%d" and name "%s" was found.\n' % (order['id'],
                                                                             order['name']))
                # 全件読み込むためにlimitにoffsetを足してループ
                statement.offset += statement.limit
            else:
                break

    # オーダーを作成する
    def create_order(self, advertiser_id: int, trafficker_id: int):
        orders = [{
            'name': 'Order #%s' % uuid.uuid4(),
            'advertiserId': advertiser_id,
            'traffickerId': trafficker_id
        }]

        orders = self.__service.createOrders(orders)
        for order in orders:
            print('Order with id "%s" and name "%s" was created.'
                  % (order['id'], order['name']))
