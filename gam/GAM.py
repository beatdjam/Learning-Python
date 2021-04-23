# 認証ファイルのpathを取得
from gam.GamCompany import GamCompany
from gam.GamLineItem import GamLineItem
from gam.GamNetwork import GamNetwork
from gam.GamOrder import GamOrder
from gam.GamUser import GamUser


def main():
    GamNetwork().get_all_networks()
    GamUser().get_current_user()
    company = GamCompany()
    company.get_all_companies()
    company.create_advertiser('Advertiser by API')
    order = GamOrder()
    order.get_all_orders()
    line_item = GamLineItem()
    line_item.get_all_line_items()


if __name__ == '__main__':
    main()
