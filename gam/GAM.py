# 認証ファイルのpathを取得
from gam.GamCompany import GamCompany
from gam.GamLineItem import GamLineItem
from gam.GamNetwork import GamNetwork
from gam.GamOrder import GamOrder
from gam.GamUser import GamUser


def main():
    networks = GamNetwork().get_all_networks()
    for network in networks:
        print('Network with network code "%s" and display name "%s" was found.'
              % (network['networkCode'], network['displayName']))

    user = GamUser().get_current_user()
    print('User with ID %d, name "%s", email "%s", and role "%s" '
          'is the current user.' % (user.id, user.name, user.email, user.roleName))

    company_service = GamCompany()
    companies = company_service.get_all_companies()
    for company in companies:
        print('Company with ID "%d", name "%s", and type "%s" was found.\n' %
              (company['id'], company['name'], company['type']))
    print('\nNumber of results found: %s' % len(companies))

    created_companies = company_service.create_advertiser('Advertiser by API')
    for company in created_companies:
        print('Company with ID "%d", name "%s", and type "%s" was found.\n' %
              (company['id'], company['name'], company['type']))
        
    order_service = GamOrder()
    order_service.get_all_orders()
    line_item = GamLineItem()
    line_item.get_all_line_items()


if __name__ == '__main__':
    main()
